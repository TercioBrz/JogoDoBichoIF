
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


User = get_user_model()

class UserServices:

    @staticmethod
    def create_user_service(username,email,password,first_name):

        if User.objects.filter(email=email).exists():
            raise ValidationError("Email já Cadastrado")
        
        return User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name
        )

    @staticmethod
    def get_user_service(ID):

        user = User.objects.get(id=ID)

        data = {
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "email": user.email,
            "balance": str(user.balance),
            "date_joined": user.date_joined.isoformat(),
        }

        return data

        
