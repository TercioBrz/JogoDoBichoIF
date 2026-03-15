
from django.db import models

from django.conf import settings
from .BaseModel import ModelBase

class Bet(ModelBase):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bet")
    win = models.DecimalField(max_digits=10, decimal_places=2)
    loss = models.DecimalField(max_digits=10, decimal_places=2)
    bet = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:

        db_table = 'bet'
        ordering = ["-created_at"]


