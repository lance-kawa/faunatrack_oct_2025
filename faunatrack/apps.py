from django.apps import AppConfig
from django.conf import settings


class FaunatrackConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'faunatrack'
    
    def ready(self):
        print("AUTH USER MODEL -----")
        print(settings.AUTH_USER_MODEL)
        print("------------")
        
        # import faunatrack.signals
