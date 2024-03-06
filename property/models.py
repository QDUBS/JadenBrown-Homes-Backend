from django.db import models
from django.utils.translation import gettext_lazy as _
from account.models import Account
from housing.models import Address, Category
from lib.custom_id import custom_id
from housing.manager import PropertiesManager
from django.utils.text import slugify

from lib.resize_image import resize_image

class Property(models.Model):
    id = models.CharField(max_length=10, primary_key=True, default=custom_id, editable=False)
    title = models.CharField(_("title of the house"),max_length=50)
    owner = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name="property_owner")
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="propert_address")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="propert_address", null=True)
    banner = models.ImageField(_("main image"), upload_to="listings", null=True, blank=True)
    description = models.TextField(_("description of the property"))
    price = models.FloatField()
    terms_and_condition = models.CharField(max_length=400)
    is_available = models.BooleanField(default=True)
    is_sold = models.BooleanField(default=False)
    is_negotiable = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    objects = models.Manager()
    available = PropertiesManager()
    
    class Meta:
        verbose_name_plural = "Properties"


    def __str__(self) -> str:
        return self.title
    

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.title}-{self.id}")
        return super().save(*args, **kwargs)
    
class Images(models.Model):
    id = models.CharField(max_length=10, primary_key=True, default=custom_id, editable=False)
    image = models.ImageField(_("image"), upload_to="listings")
    property = models.ForeignKey(Property, on_delete=models.DO_NOTHING, related_name="property_images")

    class Meta:
        verbose_name_plural = "House Images"
        
    def __str__(self) -> str:
        try:
            return f"image for {self.property.title}"
        except:
            return self.id
        
    def save(self, *args, **kwargs):
        self.image = resize_image(self.image)
        return super().save(*args, **kwargs)