from django.db.models.signals import pre_delete
from property.models import Property, Images
from housing.models import Address
from django.dispatch import receiver


@receiver(pre_delete, sender=Property)
def pre_delete_handler(sender, instance, *args, **kwargs):
    try:
        Address.objects.get(id=instance.id).delete()
        Images.objects.filter(property=instance.id).delete()
    except Exception as e:
        print(e)
        return
