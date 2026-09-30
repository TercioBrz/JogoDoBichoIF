from django.urls import path
from .views import main_bet_view, bets,extrato

urlpatterns = [
    path("main/",main_bet_view,name="Main"),
    path('bets/',bets,name="Bets"),
    path('extract/',extrato),
]