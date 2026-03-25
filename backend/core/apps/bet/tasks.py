import logging
from celery import shared_task
from django.db import transaction

from .models.FilaModel import FilaRequest
from .services.bet_core import processar_dados

logger = logging.getLogger(__name__)


@shared_task
def processar_fila():
    with transaction.atomic():
        apostas = list(
            FilaRequest.objects.select_for_update(skip_locked=True)
            .filter(status='pendente')[:100]
        )

        for aposta in apostas:
            try:
                processar_dados(aposta.user_id, aposta.dados)
                aposta.status = 'processado'
            except Exception as e:
                logger.exception(f"Erro ao processar aposta {aposta.id}: {e}")
                aposta.status = 'erro'
            aposta.save()

    if FilaRequest.objects.filter(status='pendente').exists():
        processar_fila.delay()
