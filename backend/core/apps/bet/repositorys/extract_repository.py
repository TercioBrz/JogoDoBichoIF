from django.db.models import F

from django.db import transaction
from ...users.models.TransactionModel import *
from ...users.models.UserModel import *

class TransactionRepository:

    @staticmethod
    def set_deposit_by_id_user(id_user, deposit):

        try:
            with transaction.atomic():

                user = User.objects.select_for_update().get(id=id_user)

                user.balance  = F('balance') + deposit
                user.save()

                return Transaction.objects.create(
                    user_id=id_user,
                    deposit=deposit)

        except NotImplemented as e:
            return None

    @staticmethod
    def withdrawal_by_user(id_user, withdrawal):

        try:
            with transaction.atomic():

                updated = User.objects.filter(
                    id=id_user,
                    balance__gte=withdrawal
                ).update(balance=F('balance') - withdrawal)

                if not updated:
                    return False

                return  Transaction.objects.create(
                    user_id=id_user,
                    withdrawal=withdrawal
                )

        except NotImplementedError as e:
            return False

transactionrepository = TransactionRepository()