

class BetNumbersChecks:

    def __init__(self, milhares_sorteadas):
        self.milhares_sorteadas = milhares_sorteadas

    def modalidade_grupo(self,animal,head=False):

        win: dict[str,float] = dict()

        if head:

            N = self.milhares_sorteadas[0]

            for n in animal:
                if N.endswith(n):
                    print(N,n)
                    win["group"] = 18

        else:

            for n in animal:
                for m in self.milhares_sorteadas:
                    if m.endswith(n):
                        win["group"] = 3.6

        return win

    def modalidade_dezena(self,dezena,head=False):

        win: dict[str, float] = dict()

        if head:

            N = self.milhares_sorteadas[0]

            for n in dezena:
                if N.endswith(n):
                    print(N, n)
                    win[f"{n}"] = 60

        else:

            for n in dezena:
                for m in self.milhares_sorteadas:
                    if m.endswith(n):
                        win[f"{n}"] = 12

        return win

    def modalidade_centena(self,centena,head=False):

        win: dict[str, float] = dict()

        if head:

            N = self.milhares_sorteadas[0]

            for n in centena:
                if N.endswith(n):
                    print(N, n)
                    win[f"{n}"] = 600

        else:

            for n in centena:
                for m in self.milhares_sorteadas:
                    if m.endswith(n):
                        win[f"{n}"] = 120

        return win

    def modalidade_milhar(self,milhar,head=False):

        win: dict[str, float] = dict()

        if head:

            N = self.milhares_sorteadas[0]

            for n in milhar:
                if N.endswith(n):
                    # print(N, n)
                    win[f"{n}"] = 4000

        else:

            for n in milhar:
                for m in self.milhares_sorteadas:
                    if m.endswith(n):
                        win[f"{n}"] = 800

        return win

    def modalidade_duque_grupo(self,animais):

        win: dict[str, float] = dict()

        acertos = 0
        for n in animais:
            for m in self.milhares_sorteadas:
                if m.endswith(n):
                    acertos+=1
                    break

        if acertos == 2:
            win["duque"] = 12.5

        return win

    def modalidade_duque_dezena(self,dezenas):

        win: dict[str, float] = dict()

        acertos = 0
        for n in dezenas:
            for m in self.milhares_sorteadas:
                if m.endswith(n):
                    acertos += 1
                    break

        if acertos == 2:
            win["duque"] = 800

        return win

    def modalidade_terno_grupo(self,animais):

        win: dict[str, float] = dict()

        acertos = 0
        for n in animais:
            for m in self.milhares_sorteadas:
                if m.endswith(n):
                    acertos += 1
                    break

        if acertos == 3:
            win["terno"] = 120

        return win

    def modalidade_terno_dezena(self, dezenas):

        win: dict[str, float] = dict()

        acertos = 0
        for n in dezenas:
            for m in self.milhares_sorteadas:
                if m.endswith(n):
                    acertos += 1
                    break

        if acertos == 3:
            win["terno"] = 3000

        return win











