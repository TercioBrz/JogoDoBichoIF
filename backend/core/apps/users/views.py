import datetime

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_http_methods
from .serializers import UserCreateSerializer
from django.http import JsonResponse
from .services.user_services import UserServices
from .services.auth_services import AuthServices
from .jwt_utils import generate_tokens, decode_token
from django.core.exceptions import ValidationError
import json
import jwt

@csrf_exempt
@require_POST
def create_user_view(request):
    try:
        body = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"errors": "Body inválido"}, status=400)

    serializer = UserCreateSerializer(body)

    if not serializer.is_valid():
        return JsonResponse({"errors": serializer.errors}, status=400)

    try:
        user = UserServices.create_user_service(**serializer.validated_data)

        tokens = generate_tokens(user.id)

        return JsonResponse({
            "id": user.id,
            "access_token": tokens["access_token"],
            "access_exp": tokens["access_exp"].isoformat(),
            "refresh_token": tokens["refresh_token"],
            "refresh_exp": tokens["refresh_exp"].isoformat(),
        }, status=201)

    except ValidationError as e:
        return JsonResponse({"errors": e.messages}, status=400)

@csrf_exempt
@require_POST
def login_view(request):

    try:
        body = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Body inválido"}, status=400)

    username = body.get("username")
    password = body.get("password")

    if not username or not password:
        return JsonResponse({"error": "Username e password obrigatórios"}, status=400)

    tokens = AuthServices.login_service(username, password)

    if tokens is None:
        return JsonResponse({"error": "Usuário Não encontrado"}, status=401)

    return JsonResponse({
        "access_token": tokens["access_token"],
        "access_exp": tokens["access_exp"].isoformat(),
        "refresh_token": tokens["refresh_token"],
        "refresh_exp": tokens["refresh_exp"].isoformat(),
    }, status=200)

@csrf_exempt
@require_POST
def logout_view(request):
    auth_header = request.headers.get("Authorization")

    if not auth_header or not auth_header.startswith("Bearer "):
        return JsonResponse({"error": "Token não fornecido"}, status=401)

    token = auth_header.split(" ")[1]
    AuthServices.logout_service(token)

    return JsonResponse({"menssage": "Logout realizado com sucesso"}, status=200)

@csrf_exempt
@require_POST
def refresh_view(request):
    try:
        body = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Body inválido"}, status=400)

    refresh_token = body.get("refresh_token")

    if not refresh_token:
        return JsonResponse({"error": "Refresh token obrigatório"}, status=400)

    if AuthServices.is_blacklisted(refresh_token):
        return JsonResponse({"error": "Token inválido"}, status=401)

    try:
        payload = decode_token(refresh_token)

        if payload.get("type") != "refresh":
            return JsonResponse({"erro": "Use o refresh token"}, status=401)

        tokens = generate_tokens(payload["user_id"])
        return JsonResponse({"access_token": tokens["access_token"]}, status=200)

    except jwt.ExpiredSignatureError:
        return JsonResponse({"error": "Refresh token expirado"}, status=401)
    except jwt.InvalidTokenError:
        return JsonResponse({"error": "Token inválido"}, status=401)

@csrf_exempt
@require_http_methods(["GET"])
def me_view(request):
    user = UserServices.get_user_service(request.jwt_user_id)
    return JsonResponse(user, status=200)
