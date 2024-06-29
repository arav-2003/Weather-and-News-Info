from django.apps import AppConfig


class WeatherConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weather'

from django.apps import AppConfig

def ready(self):
        import weather.signals
