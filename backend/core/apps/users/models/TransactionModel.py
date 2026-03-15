
from django.db import models
from decimal import Decimal
from django.conf import settings
from .BaseModel import ModelBase

class Transaction(ModelBase):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="transaction")
    deposit = models.DecimalField(max_digits=10,decimal_places=2,default=Decimal("0.00"))
    withdrawal = models.DecimalField(max_digits=10,decimal_places=2,default=Decimal("0.00"))

    class Meta:
        db_table = "transaction"
        ordering = ["created_at"]

