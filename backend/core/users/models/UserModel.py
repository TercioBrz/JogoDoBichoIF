from django.db import models

class Modelbase(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
class User(Modelbase):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    score = models.DecimalField(decimal_places=2, max_digits=10,default=0)

    def __str__(self):
        return self.username
