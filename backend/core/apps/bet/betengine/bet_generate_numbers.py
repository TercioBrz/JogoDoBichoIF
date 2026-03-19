import json
import random as rd
from ..redis_client import r
from .bet_times import rodada_atual
def gerar_cinco_milhares():

    milhares_sorteadas = list()

    sorteadas:set[str] = set()

    while len(milhares_sorteadas) < 5:
        numero = list()
        while len(numero) < 2:
            n = f"{rd.randint(0, 99):02}"

            if n not in sorteadas:
                numero.append(n)
                sorteadas.add(n)

        milhares_sorteadas.append(''.join(numero))

    r.set(f"{rodada_atual()}",json.dumps(milhares_sorteadas),ex=1800)

    return milhares_sorteadas

