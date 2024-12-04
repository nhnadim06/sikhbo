# base/apps.py
from django.apps import AppConfig

class BaseConfig(AppConfig):
    name = 'base'

    def ready(self):
        import base.signals  # This will load the signals when the app is ready
