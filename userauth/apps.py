from django.apps import AppConfig


class UserauthConfig(AppConfig):
    name = 'userauth'
    
    def ready(self):
        from .signals import handlers 