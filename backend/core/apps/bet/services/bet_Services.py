
from ...users.models.BetModel import Bet
from ...users.jwt_utils import decode_token
from ...users.models.UserModel import User

from django.db.models import F

class ServiceBet:

    def __init__(self, request,data):
        self.token = decode_token(request.headers['Authorization'].split()[1])
        self.data = data

    def check_saldo(self):
        user = User.objects.get(id=self.token["user_id"])

        if self.data["aposta"] > user.balance:
            return False

        return True

    def calcular_ganhos_ou_perdas(self, ganhos, aposta):

        ganho = 0

        for k in ganhos:
            ganho = ganhos[k] * aposta

        if ganho > 0:
            Bet.objects.create(
                user_id=self.token["user_id"],
                win=ganho,
                loss=0,
                bet=aposta,
            )
            User.objects.filter(id=self.token["user_id"]).update(
                balance=F('balance') + ganho - aposta
            )

        else:
            Bet.objects.create(
                user_id=self.token["user_id"],
                win=0,
                loss=aposta,
                bet=aposta,
            )
            User.objects.filter(id=self.token["user_id"]).update(
                balance=F('balance') - aposta
            )

        return ganho