import random as rd

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

    return milhares_sorteadas

