from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from .models import User

def validate_email_user(email):

    validator = EmailValidator()

    try:
        validator(email)

    except ValidationError as e:
        return e.messages

    return None


def validate_password_user(password, username , first_name ,email):

    user = User (
        username=username,
        first_name=first_name,
        email=email
    )

    try:
        validate_password(password,user=user)

    except ValidationError as e:
        return e.messages

    return None