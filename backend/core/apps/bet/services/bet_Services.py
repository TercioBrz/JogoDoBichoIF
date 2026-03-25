
from ...users.models.BetModel import Bet
from ...users.models.UserModel import User
from django.db.models import F
from django.db import transaction

class ServiceBet:
    def __init__(self,user_id,data):

        self.user:str = user_id
        self.data = data

    def check_saldo(self):
        user = User.objects.get(id=self.user)

        return self.data["aposta"] <= user.balance

    def calcular_ganhos_ou_perdas(self,ganhos):

        ganho = 0

        for k in ganhos.keys():
            ganho = ganhos[k] * self.data['aposta']

        with transaction.atomic():
            if ganho > 0:
                Bet.objects.create(
                    user_id=self.user,
                    win=ganho,
                    loss=0,
                    bet=self.data['aposta'],
                )
                User.objects.filter(id=self.user).update(
                    balance=F('balance') + ganho - self.data['aposta']
                )

            else:
                Bet.objects.create(
                    user_id=self.user,
                    win=0,
                    loss=self.data['aposta'],
                    bet=self.data['aposta'],
                )

                User.objects.filter(id=self.user).update(
                    balance=F('balance') - self.data['aposta']
                )
