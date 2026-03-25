import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from apps.bet.services.bet_Services import ServiceBet
from .models.FilaModel import FilaRequest
from django.views.decorators.http import require_POST, require_http_methods

from ..users.jwt_utils import decode_token


@csrf_exempt
def main_bet_view(request):
    MODALIDADES_VALIDAS = {
        "grupo", "dezena", "centena", "milhar",
        "duque_grupo", "duque_dezena", "terno_grupo", "terno_dezena"
    }

    body = json.loads(request.body)
    header = request.headers.get("Authorization")

    user = decode_token(header.split(" ")[1])

    chave = list(body.get("modalidade").keys())[0]
    if chave not in MODALIDADES_VALIDAS:
        return JsonResponse({"success": False, "message": "Modalidade inválida"}, status=400)

    bet = ServiceBet(user["user_id"], body)
    if not bet.check_saldo():
        return JsonResponse({"success": False, "message": "Saldo insuficiente"}, status=400)

    FilaRequest.objects.create(
        user_id=user["user_id"],
        dados=body,
        status='pendente'
    )

    return JsonResponse({"success": True, "message": "Aposta enfileirada"}, status=202)
@csrf_exempt
def bets(request):
    pass

@csrf_exempt
def extrato(request):
    pass

@csrf_exempt
@require_http_methods(["PATCH"])
def transactions_bet(request):

    body = json.loads(request.body)

    if body.get("action") == "deposit":
        pass

    elif body.get("action") == "withdraw":
        pass

    else:
        return  None
