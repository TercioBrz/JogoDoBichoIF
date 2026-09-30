from django.http import JsonResponse
from .jwt_utils import decode_token
from django.contrib.auth import get_user_model
import jwt

User = get_user_model()

class JWTAuthMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        public_routes = ["/api/auth/login/", "/api/auth/refresh/", "/api/auth/register/", "/api/auth/logout/"]

        if request.path in public_routes:
            return self.get_response(request)

        token = request.headers.get("Authorization",None)
        token = token.split(" ")[1] if token else None

        print(token)

        if not token:
            return JsonResponse({"errors": "Token não fornecido"}, status=401)

        try:
            payload = decode_token(token)

            if payload.get("type") != "access":
                return JsonResponse({"errors": "Use o access token"}, status=401)

            user = payload["user_id"]

            request.user = user

        except jwt.ExpiredSignatureError:
            return JsonResponse({"errors": "Token expirado"}, status=401)

        except jwt.InvalidTokenError as e:
            print("ERRO JWT:", type(e).__name__, str(e))
            return JsonResponse(
                {"errors": "Token invalido mid"},
                status=401
            )

        return self.get_response(request)