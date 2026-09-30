
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db.models import Q

from apps.users.repositorys.user_repository import userrepository

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
    def me(user_id):

        user = userrepository.get_user_by_id(user_id)

        data = {
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "email": user.email,
            "balance": str(user.balance),
            "date_joined": user.date_joined.isoformat(),
        }

        return data

        
