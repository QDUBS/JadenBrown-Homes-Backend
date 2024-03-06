from django.db.models import Manager
from django.db.models.query import QuerySet

class PropertiesManager(Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(is_available=True, is_sold=False)