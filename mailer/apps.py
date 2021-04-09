from django.apps import AppConfig


class MailerConfig(AppConfig):
    name = 'mailer'
     def ready(self):
        from . import scheduler
        if settings.SCHEDULER_AUTOSTART:
        	scheduler.start()
    