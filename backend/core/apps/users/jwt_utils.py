import jwt
import datetime
from django.conf import settings

ACCESS_TOKEN_EXPIRY = datetime.timedelta(minutes=15)
REFRESH_TOKEN_EXPIRY = datetime.timedelta(days=7)

def generate_tokens(user_id):

    now = datetime.datetime.now(datetime.timezone.utc)

    access_token = jwt.encode({
        "user_id": user_id,
        "iat": now,
        "exp": now + ACCESS_TOKEN_EXPIRY,
        "type": "access"
    }, settings.SECRET_KEY, algorithm="HS256")

    refresh_token = jwt.encode({
        "user_id": user_id,
        "iat": now,
        "exp": now + REFRESH_TOKEN_EXPIRY,
        "type": "refresh"
    }, settings.SECRET_KEY, algorithm="HS256")

    return {
        "access_token": access_token,
        "access_exp": now + ACCESS_TOKEN_EXPIRY,
        "refresh_token": refresh_token,
        "refresh_exp": now + REFRESH_TOKEN_EXPIRY
    }

def decode_token(token):
    return jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])