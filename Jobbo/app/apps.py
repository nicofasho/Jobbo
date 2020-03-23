from django.apps import AppConfig

class JobConfig(AppConfig):
    name = 'app'

    def ready(self):
        from .scheduler import start_background_job
        start_background_job()


        
