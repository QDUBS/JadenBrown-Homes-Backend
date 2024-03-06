from django.db.models.signals import pre_delete
from django.dispatch import receiver
from housing.models import Address, House, Features

@receiver(pre_delete,sender=House)
def pre_delete_handler(sender, instance, *args, **kwargs):
    try:
        Address.objects.get(id=instance.id).delete()
        Features.objects.get(id=instance.id).delete()
    except:
        pass