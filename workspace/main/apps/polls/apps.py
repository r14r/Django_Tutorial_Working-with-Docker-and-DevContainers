from django.apps import AppConfig


class PollsConfig(AppConfig):
    name = 'apps.polls'
    verbose_name = 'Polling App'

    default_auto_field = 'django.db.models.BigAutoField'
    