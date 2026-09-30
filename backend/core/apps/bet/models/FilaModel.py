from django.db import models
from ...users.models.BaseModel import ModelBase

class Status(models.TextChoices):
    PENDENTE = 'pendente', 'Pendente'
    PROCESSADO = 'processado', 'Processado'
    ERROR = 'error', 'Error'

class FilaRequest(ModelBase):

    user_id = models.IntegerField()
    dados = models.JSONField()
    status = models.CharField(choices=Status.choices, default=Status.PENDENTE)
