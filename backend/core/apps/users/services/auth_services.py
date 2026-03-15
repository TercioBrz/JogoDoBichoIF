
from django.contrib.auth import get_user_model, authenticate
from ..jwt_utils import generate_tokens
from ..models.BlacListModel import TokenBlacklist

User = get_user_model()

class AuthServices:

    @staticmethod
    def login_service(username, password):

        user = authenticate(username=username, password=password)

        if user is None:
            return None

        tokens = generate_tokens(user.id)

        return tokens

    @staticmethod
    def logout_service(token):
        TokenBlacklist.objects.get_or_create(token=token)

    @staticmethod
    def is_blacklisted(token):
        return TokenBlacklist.objects.filter(token=token).exists()