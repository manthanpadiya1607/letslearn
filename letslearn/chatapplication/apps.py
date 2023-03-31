from django.apps import AppConfig


class ChatapplicationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chatapplication'

class ProfilesConfig(AppConfig):
    name = 'profiles'
    def ready(self):
        import chatapplication.signals
