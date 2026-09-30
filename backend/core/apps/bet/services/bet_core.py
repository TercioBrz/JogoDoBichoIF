import json

from ..betengine.bet_numbers_checks import BetNumbersChecks as Bt
from ...bet.utils import rodada_atual
from ..services.bet_Services import ServiceBet
from ..redis_client import r


def processar_dados(user_id, body):

    sorteados = json.loads(r.get(rodada_atual()))

    bt = Bt(sorteados)

    mod = body["modalidade"]

    modalidade_map = {
        "grupo":        lambda: bt.modalidade_grupo(body['grupo'], body.get('head', False)),
        "dezena":       lambda: bt.modalidade_dezena(body['dezena'], body.get('head', False)),
        "centena":      lambda: bt.modalidade_centena(body['centena'], body.get('head', False)),
        "milhar":       lambda: bt.modalidade_milhar(body['milhar'], body.get('head', False)),
        "duque_grupo":  lambda: bt.modalidade_duque_grupo(body['duque_grupo']),
        "duque_dezena": lambda: bt.modalidade_duque_dezena(body['duque_dezena']),
        "terno_grupo":  lambda: bt.modalidade_terno_grupo(body['terno_grupo']),
        "terno_dezena": lambda: bt.modalidade_terno_dezena(body['terno_dezena']),
    }

    bet = ServiceBet(user_id, body)

    ganhos: dict[str, int] = modalidade_map[mod]()

    bet.calcular_ganhos_ou_perdas(ganhos)