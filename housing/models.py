from django.db import models
from django.utils.translation import gettext_lazy as _
from account.models import Account
from lib.custom_id import custom_id
from django.utils.text import slugify
from housing.manager import PropertiesManager
from lib.resize_image import resize_image


class Address(models.Model):
    id = models.CharField(max_length=10, primary_key=True, default=custom_id, editable=False)
    state = models.CharField(_("state"),max_length=20)
    city = models.CharField(_("city"),max_length=20)
    town = models.CharField(_("town"),max_length=20)
    description = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.state

class Category(models.Model):
    id = models.CharField(max_length=10, primary_key=True, default=custom_id, editable=False)
    name = models.CharField(_("category"), max_length=20)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name


class HouseType(models.Model):
    id = models.CharField(max_length=10, primary_key=True, default=custom_id, editable=False)
    type = models.CharField(_("type of house"), max_length=20)

    def __str__(self) -> str:
        return self.type


class Features(models.Model):
    id = models.CharField(max_length=10, primary_key=True, default=custom_id, editable=False)
    bedrooms = models.IntegerField(_("number of bedrooms"), null=True, blank=True)
    bathrooms = models.IntegerField(_("number of bathrooms"), null=True, blank=True)
    packing_space = models.IntegerField(_("number of packing space"), null=True, blank=True)
    balcony = models.BooleanField(default=True)
    more_details = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.id)


class House(models.Model):
    id = models.CharField(max_length=10, primary_key=True, default=custom_id, editable=False)
    title = models.CharField(_("title of the house"),max_length=50)
    owner = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name="house_owner")
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="house_address")
    category = models.ForeignKey(Category,  on_delete=models.CASCADE, related_name="category")
    features = models.OneToOneField(Features, null=True, blank=True, related_name="house_features", on_delete=models.SET_NULL)
    banner = models.ImageField(_("main image"), upload_to="listings", null=True, blank=True)
    type = models.ForeignKey(HouseType, on_delete=models.SET_NULL, null=True)
    description = models.TextField(_("description of the house"))
    price = models.FloatField()
    terms_and_condition = models.CharField(max_length=400)
    is_available = models.BooleanField(default=True)
    is_sold = models.BooleanField(default=False)
    is_negotiable = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Houses"

    objects = models.Manager()
    available = PropertiesManager()

    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.title}-{self.id}")
        return super().save(*args, **kwargs)
    
   

class Images(models.Model):
    id = models.CharField(max_length=10, primary_key=True, default=custom_id, editable=False)
    image = models.ImageField(_("image"), upload_to="listings")
    house = models.ForeignKey(House, on_delete=models.DO_NOTHING, related_name="house_images")

    class Meta:
        verbose_name_plural = "House Images"

    def __str__(self) -> str:
        try:
            return f"image for {self.house.title}"
        except:
            return self.id
        

    def save(self,*args, **kwargs ):
        self.image = resize_image(self.image)
        return super().save(*args, **kwargs)