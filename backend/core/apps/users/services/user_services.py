
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db.models import Q


User = get_user_model()

class UserServices:

    @staticmethod
    def create_user_service(username,email,password,first_name):

        users = User.objects.filter(Q(email=email) | Q(username=username))

        error = {}

        for user in users:

            if user.email == email:
                error["email"] = "Email ja registrado"

            if user.username == username:
                error["username"] = "Username ja registrado"

        if error:
            raise ValidationError(error)
        
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

        
