def set_refresh_token_cookie(response, token):

    response.set_cookie(
        "refresh_token",
        token["refresh_token"],
        httponly=True,
        samesite="Lax",
        expires=token["refresh_exp"],
        secure=False,
    )
    return response

