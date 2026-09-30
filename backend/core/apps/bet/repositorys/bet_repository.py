
from ...users.models.BetModel import *

class BetRepository:

    @staticmethod
    def get_bets_by_id(id_user):

        return Bet.objects.filter(user_id=id_user).values()

betrepository = BetRepository()