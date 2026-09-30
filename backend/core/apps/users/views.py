from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_http_methods
from .serializers import UserCreateSerializer, UserLoginSerializer
from django.http import JsonResponse
from .services.user_services import UserServices
from .services.auth_services import AuthServices
from .jwt_utils import generate_tokens, decode_token
from django.core.exceptions import ValidationError
import json
import jwt
from ..utils.token_cookie_utils import set_refresh_token_cookie

@csrf_exempt
@require_POST
def register_view(request):

    try:
        body = json.loads(request.body)

    except json.JSONDecodeError:
        return JsonResponse({
            "success": False,
            "data": "",
            "errors": {
                'JSON': "body invalido"
            },
            "message": ""

        }, status=400)

    serializer = UserCreateSerializer(body)

    if not serializer.is_valid():
        return JsonResponse({
            "success": False,
            "data": "",
            "errors": serializer.errors,
            "message": ""

        }, status=400)

    try:
        
        UserServices.create_user_service(**serializer.validated_data)

        response = JsonResponse({
            "success": True,
            "data": "",
            "errors": {},
            "message": "User criado com Sucesso!"

        }, status=201)

        return response

    except ValidationError as e:
        return JsonResponse({
            "success": False,
            "data": "",
            "errors": e.message_dict,
            "message": ""

        }, status=400)

@csrf_exempt
@require_POST
def login_view(request):

    try:
        body = json.loads(request.body)

    except json.JSONDecodeError:
        return JsonResponse({
            "success": False,
            "data": "",
            "errors": {
                'Json': "Body invalido"
            },
            "message": ""
        }, status=400)

    username = body.get("username")
    password = body.get("password")

    token = AuthServices.login_service(username, password)

    if token is None:
        return JsonResponse({
            "success": False,
            "data": "",
            "errors": {
                "User": "Usuário não encontrado"
            },
            "message": ""

        }, status=404)

    response: JsonResponse = JsonResponse({
            "success": True,
            "data": {
                "access_token": token['access_token'],
                "name": username

            },
            "errors": {},
            "message": "Login realizado com sucesso"

        }, status=200)

    return set_refresh_token_cookie(response,token) 

@csrf_exempt
@require_POST
def logout_view(request):
    refresh_token = request.COOKIES.get("refresh_token")

    if not refresh_token:
        return JsonResponse({"errors": {
        "Token":"Refresh Token não Encontrado"}
    }, status=400)

    AuthServices.logout_service(refresh_token)

    response = JsonResponse({"message": "Logout Realizado com Sucesso"}, status=200)
    response.delete_cookie("refresh_token")

    return response

@csrf_exempt
@require_POST
def refresh_view(request):
    
    refresh_token = request.COOKIES.get("refresh_token")

    if not refresh_token:
        return JsonResponse({"errors": {
            "Token": "Refresh Token não Encontrado"}
        }, status=400)

    try:
        payload = decode_token(refresh_token)

        if payload.get("type") != "refresh":
            return JsonResponse({"errors": {"Use o refresh token"}}, status=401)

        user_id = payload['user_id']
        tokens = generate_tokens(user_id)

        response = JsonResponse({

            "success": True,
            "data": {
                'access_token': tokens["access_token"],
            },
            "errors": {},
            "message": "Token Renovado"

        }, status=200)

        return set_refresh_token_cookie(response, tokens)

    except jwt.ExpiredSignatureError:
        return JsonResponse({"errors": {"Token": "Refresh Token Expirado"}}, status=401)
    except jwt.InvalidTokenError:
        return JsonResponse({"errors": {"Token": "Token Inválido"}}, status=401)

@csrf_exempt
@require_http_methods(["GET"])
def me_view(request):

    user = UserServices.me(request.user)
    return JsonResponse(user, status=200)