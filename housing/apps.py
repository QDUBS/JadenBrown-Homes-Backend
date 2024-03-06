from django.apps import AppConfig


class HousingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'housing'

    def ready(self) -> None:
        import signals.house
        return super().ready()
