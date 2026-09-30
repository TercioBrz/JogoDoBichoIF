grupos: dict[int, list[str]] = {
    1: ["00", "01", "02", "03"],
    2: ["04", "05", "06", "07"],
    3: ["08", "09", "10", "11"],
    4: ["12", "13", "14", "15"],
    5: ["16", "17", "18", "19"],
    6: ["20", "21", "22", "23"],
    7: ["24", "25", "26", "27"],
    8: ["28", "29", "30", "31"],
    9: ["32", "33", "34", "35"],
    10: ["36", "37", "38", "39"],
    11: ["40", "41", "42", "43"],
    12: ["44", "45", "46", "47"],
    13: ["48", "49", "50", "51"],
    14: ["52", "53", "54", "55"],
    15: ["56", "57", "58", "59"],
    16: ["60", "61", "62", "63"],
    17: ["64", "65", "66", "67"],
    18: ["68", "69", "70", "71"],
    19: ["72", "73", "74", "75"],
    20: ["76", "77", "78", "79"],
    21: ["80", "81", "82", "83"],
    22: ["84", "85", "86", "87"],
    23: ["88", "89", "90", "91"],
    24: ["92", "93", "94", "95"],
    25: ["96", "97", "98", "99"]
}


class BetNumbersChecks:

    def __init__(self, milhares_sorteadas):
        self.milhares_sorteadas = milhares_sorteadas

    def modalidade_grupo(self, grupo: str, head=False):

        win: dict[str, float] = dict()

        if head:

            N = self.milhares_sorteadas[0]

            ans = grupos.get(int(grupo), [])

            for v in ans:
                if N.endswith(v):
                    win["group"] = 18
                    break

        else:

            for n in grupos.get(int(grupo), []):

                for m in self.milhares_sorteadas:

                    if m.endswith(n):
                        win["grupo"] = 3.6
                        break

                if "grupo" in win:
                    break

        return win

    def modalidade_dezena(self, dezena: str, head=False):

        win: dict[str, float] = dict()

        dezena = str(dezena)

        if head:

            N = self.milhares_sorteadas[0]

            if N.endswith(dezena):
                win["dezena"] = 60

        else:

            for m in self.milhares_sorteadas:

                if m.endswith(dezena):
                    win["dezena"] = 12
                    break

        return win

    def modalidade_centena(self, centena: str, head=False):

        win: dict[str, float] = dict()

        centena = str(centena)

        if head:

            N = self.milhares_sorteadas[0]

            if N.endswith(centena):
                print(N, centena)
                win["centena"] = 600

        else:

            for m in self.milhares_sorteadas:

                if m.endswith(centena):
                    win["centena"] = 120
                    break

        return win

    def modalidade_milhar(self, milhar: str, head=False):

        win: dict[str, float] = dict()

        milhar = str(milhar)

        if head:

            N = self.milhares_sorteadas[0]

            if N.endswith(milhar):
                win["milhar"] = 4000

        else:

            for m in self.milhares_sorteadas:

                if m.endswith(milhar):
                    win["milhar"] = 800
                    break

        return win

    def modalidade_duque_grupo(self, grupo: list[str]) -> dict[str, float]:

        win: dict[str, float] = {}
        acertos = 0

        for n in grupo:

            grupo_atual = grupos.get(int(n), [])

            for m in self.milhares_sorteadas:

                if any(m.endswith(v) for v in grupo_atual):
                    acertos += 1
                    break

        if acertos == 2:
            win["duque_grupo"] = 18

        return win

    def modalidade_duque_dezena(self, dezenas: list[str]):

        win: dict[str, float] = {}
        acertos = 0

        for dezena_atual in dezenas:

            dezena_atual = str(dezena_atual)

            for m in self.milhares_sorteadas:

                if m.endswith(dezena_atual):
                    acertos += 1
                    break

        if acertos == 2:
            win["duque_dezena"] = 120

        return win

    def modalidade_terno_grupo(self, grupo: list[str]):

        win: dict[str, float] = dict()
        acertos = 0

        for n in grupo:

            grupo_atual = grupos.get(int(n), [])

            for m in self.milhares_sorteadas:

                if any(m.endswith(v) for v in grupo_atual):
                    acertos += 1
                    break

        if acertos == 3:
            win["terno_grupo"] = 1200

        return win

    def modalidade_terno_dezena(self, dezenas: list[str]):

        win: dict[str, float] = dict()
        acertos = 0

        for n in dezenas:

            n = str(n)

            for m in self.milhares_sorteadas:

                if m.endswith(n):
                    acertos += 1
                    break

        if acertos == 3:
            win["terno_dezena"] = 3000

        return win