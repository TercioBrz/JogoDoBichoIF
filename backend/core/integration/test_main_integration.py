import pytest
from django.contrib.auth import get_user_model
from . import generate_tokens

User = get_user_model()

@pytest.fixture
def customer_user(db):
    return User.objects.create_user( #Hasheada
        username="TercioBrz",
        password="neps999A",
        email="brazuca123@gmail.com",
        first_name="Tercio"
    )

@pytest.fixture
def customer_token(customer_user):
    return generate_tokens(customer_user.id)

def test_que_verifica_customer_token(customer_token):
    assert type(customer_token) == dict and customer_token['access_token']

def test_que_registrar_user(db,client):

    response = client.post("/api/auth/register/", {
        "username": "TercioBrz",
        "password": "neps999A",
        "email": "brazuca123@gmail.com",
        "first_name": "Tercio"
    }, content_type="application/json")


    assert response.status_code == 201

def test_que_passa_login(customer_user,customer_token,client):

    response = client.post("/api/auth/login/", {
        "username": customer_user.username,
        "password": "neps999A",
    }, content_type="application/json",
    headers={"Authorization": f"Bearer {customer_token['access_token']}"})

    assert response.status_code == 200


@pytest.mark.xfail(reason="Dados já Existentes")
def test_que_passa_que_falhar_registro(customer_user,client):

    response = client.post("/api/auth/register/", {
        "username": customer_user.username,
        "password": "neps999A",
        "email": customer_user.email,
        "first_name": customer_user.first_name
    }, content_type="application/json")

    assert response.json().get("errors") == {'email': ['Email ja registrado'], 'username': ['Username ja registrado']}
    assert response.status_code == 400


def test_que_passa_logout(customer_token,client,customer_user):

    refresh = customer_token["refresh_token"]

    response = client.post("/api/auth/logout/", {
        "refresh_token": refresh,
    },content_type="application/json",
    headers={"Authorization": f"Bearer {customer_token['access_token']}"})

    assert response.status_code == 200

def test_que_simula_aposta_grupo(customer_token,client,customer_user):

    response = client.post("/api/bet/main/", {

        "modalidade": {
            "grupo": ["01","02","03","04"]
        },
        "aposta": 4.5

    }, content_type="application/json",
    headers={"Authorization": f"Bearer {customer_token['access_token']}"})

    assert response.status_code == 200
