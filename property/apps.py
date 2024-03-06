from django.apps import AppConfig


class PropertyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'property'

    def ready(self) -> None:
        import signals.property
        return super().ready()
