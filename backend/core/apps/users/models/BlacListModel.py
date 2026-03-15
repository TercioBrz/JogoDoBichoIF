from django.db import models
from .BaseModel import ModelBase

class TokenBlacklist(ModelBase):
    token = models.TextField(unique=True)

    def __str__(self):
        return f"Blacklisted token at {self.created_at}"

