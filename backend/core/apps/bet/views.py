import json

from django.http import JsonResponse
from .betengine.bet_numbers_checks import BetNumbersChecks as Bt
from .betengine.bet_generate_numbers import gerar_cinco_milhares
from .services.bet_Services import ServiceBet

def main_view(request):
    data = json.loads(request.body)

    mod = data["modalidade"]

    bt = Bt(gerar_cinco_milhares())

    modalidade_map = {
        "grupo":        lambda: bt.modalidade_grupo(mod['grupo'], data.get('head', False)),
        "dezena":       lambda: bt.modalidade_dezena(mod['dezena'], data.get('head', False)),
        "centena":      lambda: bt.modalidade_centena(mod['centena'], data.get('head', False)),
        "milhar":       lambda: bt.modalidade_milhar(mod['milhar'], data.get('head', False)),
        "duque_grupo":  lambda: bt.modalidade_duque_grupo(mod['duque_grupo']),
        "duque_dezena": lambda: bt.modalidade_duque_dezena(mod['duque_dezena']),
        "terno_grupo":  lambda: bt.modalidade_terno_grupo(mod['terno_grupo']),
        "terno_dezena": lambda: bt.modalidade_terno_dezena(mod['terno_dezena']),
    }

    modalidade_escolhida = list(mod.keys())[0]

    if modalidade_escolhida not in modalidade_map:
        return JsonResponse({"success": False, "message": "Modalidade inválida"}, status=400)

    bet = ServiceBet(request,data)

    if not bet.check_saldo():
        return JsonResponse({"success": False, "message": "Saldo insuficiente"}, status=400)

    ganhos = modalidade_map[modalidade_escolhida]()

    wins = bet.calcular_ganhos_ou_perdas(ganhos, data['aposta'])

    return JsonResponse({"success": True, "ganhos": wins}, status=200)