from django.http import JsonResponse
from .jwt_utils import decode_token
from .services.auth_services import AuthServices
from django.contrib.auth import get_user_model
import jwt

User = get_user_model()

class JWTAuthMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        public_routes = ["/api/auth/login/", "/api/auth/refresh/", "/api/auth/register/",]

        if request.path in public_routes:
            return self.get_response(request)

        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return JsonResponse({"error": "Token não fornecido"}, status=401)

        token = auth_header.split(" ")[1]

        if AuthServices.is_blacklisted(token):
            return JsonResponse({"error": "Token inválido"}, status=401)

        try:
            payload = decode_token(token)

            if payload.get("type") != "access":
                return JsonResponse({"error": "Use o access token"}, status=401)

            request.jwt_user_id = payload["user_id"]
            # request.user = User.objects.get(id=payload["user_id"])

        except jwt.ExpiredSignatureError:
            return JsonResponse({"error": "Token expirado"}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({"error": "Token inválido"}, status=401)

        return self.get_response(request)