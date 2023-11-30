from django.apps import AppConfig


class CsmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CSM'

    def ready(self):
        import CSM.signals
