from ..betengine.bet_numbers_checks import BetNumbersChecks as Bt
from ...bet.utils import rodada_atual
from ..services.bet_Services import ServiceBet
from ..redis_client import r


def processar_dados(user_id, body):
    bt = Bt(r.get(rodada_atual()))
    mod = body["modalidade"]

    modalidade_map = {
        "grupo":        lambda: bt.modalidade_grupo(mod['grupo'], body.get('head', False)),
        "dezena":       lambda: bt.modalidade_dezena(mod['dezena'], body.get('head', False)),
        "centena":      lambda: bt.modalidade_centena(mod['centena'], body.get('head', False)),
        "milhar":       lambda: bt.modalidade_milhar(mod['milhar'], body.get('head', False)),
        "duque_grupo":  lambda: bt.modalidade_duque_grupo(mod['duque_grupo']),
        "duque_dezena": lambda: bt.modalidade_duque_dezena(mod['duque_dezena']),
        "terno_grupo":  lambda: bt.modalidade_terno_grupo(mod['terno_grupo']),
        "terno_dezena": lambda: bt.modalidade_terno_dezena(mod['terno_dezena']),
    }

    modalidade_escolhida = list(mod.keys())[0]
    bet = ServiceBet(user_id, body)
    ganhos = modalidade_map[modalidade_escolhida]()
    bet.calcular_ganhos_ou_perdas(ganhos)