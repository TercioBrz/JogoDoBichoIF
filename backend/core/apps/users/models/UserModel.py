from django.contrib.auth.models import AbstractUser
from django.db import models
from decimal import Decimal


class User(AbstractUser):

    balance = models.DecimalField(max_digits=10,decimal_places=2,default=Decimal("100.00"))

    class Meta:
        db_table = "custom_user"
        ordering = ["date_joined"]
