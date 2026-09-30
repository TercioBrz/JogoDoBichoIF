from django.contrib.auth import get_user_model
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

def validate_email_user(email):

    validator = EmailValidator()

    try:
        validator(email)

    except ValidationError as e:
        return e.messages

    return []

def validate_password_user(password, username , first_name=None ,email=None):

    user = User (
        username=username,
        first_name=first_name,
        email=email
    )

    try:
        validate_password(password,user=user)

    except ValidationError as e:
        return e.messages

    return []

def validate_strong_password(password):

    password_valid = {
        'IsUpper': 'No minimo um caracter Maiusculo',
        'IsLower': 'No minimo um caracter Minusculo',
        'IsNumber': 'No minimo um Numero',
    }

    for char in password:

        if char.isupper() and password_valid.get('IsUpper'):
            del password_valid['IsUpper']

        if char.islower() and password_valid.get('IsLower'):
            del password_valid['IsLower']

        if char.isdigit() and password_valid.get('IsNumber'):
            del password_valid['IsNumber']

    return list(password_valid.values())







