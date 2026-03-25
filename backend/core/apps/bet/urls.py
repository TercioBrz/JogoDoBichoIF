from django.urls import path
from .views import main_bet_view

urlpatterns = [
    path("main/",main_bet_view,name="Main"),
]