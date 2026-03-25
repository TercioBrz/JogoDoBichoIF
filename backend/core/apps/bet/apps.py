from django.apps import AppConfig


class BetConfig(AppConfig):
    name = 'apps.bet'

    def ready(self):
        import apps.bet.betengine
