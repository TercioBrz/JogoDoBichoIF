from django.urls import path
from .views import *

urlpatterns = [
    path("register/",create_user_view,name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("refresh/", refresh_view, name="refresh"),
    path("me/", me_view, name="me")
]

