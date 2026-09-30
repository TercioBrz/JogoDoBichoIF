import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from apps.bet.services.bet_Services import ServiceBet
from .models.FilaModel import FilaRequest
from django.views.decorators.http import require_POST, require_http_methods, require_GET
from ..users.jwt_utils import decode_token
from .repositorys import *

@csrf_exempt
@require_POST
def main_bet_view(request):
    
    MODALIDADES_VALIDAS = {
        "grupo", "dezena", "centena", "milhar",
        "duque_grupo", "duque_dezena", "terno_grupo", "terno_dezena"
    }

    try:
        body = json.loads(request.body)

    except json.JSONDecodeError:
        return JsonResponse({
            "success": False,
            "data": "",
            "errors": {
                'Json': "body invalido"
            },
            "message": ""
        }, status=400)

    user_id = request.user

    chave = body.get("modalidade")

    if chave not in MODALIDADES_VALIDAS:
        return JsonResponse({"success": False, "message": "Modalidade inválida"}, status=400)

    bet = ServiceBet(user_id, body)

    if not bet.check_saldo():
        return JsonResponse({"success": False, "message": "Saldo insuficiente"}, status=400)

    FilaRequest.objects.create(
        user_id=user_id,
        dados=body,
        status='pendente'
    )
    print("Criado")

    return JsonResponse({"success": True, "message": "Aposta enfileirada"}, status=202)

@csrf_exempt
@require_GET
def bets(request):

    token = request.headers.get('Authorization').split()[1]

    user = decode_token(token)

    bets_user = betrepository.get_bets_by_id(user["user_id"])

    return JsonResponse({'bets': list(bets_user)}, status=200)

@csrf_exempt
def extrato(request):

    bets = Bet.objects.filter(
    user_id=request.user
        ).values(

            "win",
            "loss",
            "bet",
            "created_at"
        )

    return JsonResponse({
        "data": list(bets)
    })

@csrf_exempt
@require_http_methods(["PATCH"])
def transactions_bet(request):

    try:
        body = json.loads(request.body)

    except json.JSONDecodeError:
        return JsonResponse({
            "success": False,
            "data": "",
            "errors": {
                'json': "body invalido"
            },
            "message": ""
        }, status=400)

    if body.get("action") == "deposit":

        deposit = body['action']['deposit']

        transaction_ok = TransactionRepository.set_deposit_by_id_user(request.user,body['action']['deposit'])

        if transaction_ok:

            return JsonResponse({
                'success': True,
                'data': {

                    'deposit': deposit
                },
                'errors': {},
                'message': 'Deposito realizado com sucesso!'

            },status=200)

        return JsonResponse({},status=400)


    elif body.get("action") == "withdraw":

        withdraw = body['action']['withdraw']

        transaction_ok = TransactionRepository.set_deposit_by_id_user(request.user, body['action']['withdraw'])

        if transaction_ok:
            return JsonResponse({
                'success': True,
                'data': {
                    'deposit': withdraw
                },
                'errors': {},
                'message': 'Saque realizado com sucesso!'

            }, status=200)

        return  JsonResponse({},status=400)

    return JsonResponse({
        'success': False,
        'data': {},
        'errors': {
            'transaction': "Operação Invalida"
        },
        'message': ''

    }, status=400)

