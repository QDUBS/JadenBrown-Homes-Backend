from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from lib.custom_id import custom_id

from .manager import AccountManager

class Account(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(unique=True, primary_key=True, default=custom_id, max_length=100, editable=False)
    email = models.EmailField(_("Email Adress"), max_length=100, unique=True)
    username = models.CharField(_("Username"), max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_oauth = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD= "email"
    REQUIRED_FIELDS = ["username"]

    objects = AccountManager()

    def __str__(self):
        return self.email

class Contact(models.Model):
    id = models.CharField(unique=True, primary_key=True, default=custom_id, max_length=100, editable=False)
    phone_one = models.CharField(max_length=15)    
    phone_two = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(_("Business Email"), blank=True, null=True)   
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.phone_one

class Address(models.Model):
    id = models.CharField(unique=True, primary_key=True, default=custom_id, max_length=100, editable=False)
    state = models.CharField(_("State"), max_length=20)
    city = models.CharField(_("city"), max_length=20)
    street = models.CharField(_("street"), max_length=20)
    description = models.CharField(_("Description"), max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return  self.street
    

class AccountProfile(models.Model):
    choices = (
        ("regualar", "regular"),
        ("agent", "agent"),
    )
    id = models.CharField(unique=True, primary_key=True, default=custom_id, max_length=100, editable=False)
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="user_profile")
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="contact")
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="address")
    first_name = models.CharField(_("First Name"), max_length=255)
    last_name = models.CharField(_("Last Name"), max_length=255)
    nickname = models.CharField(_("Nick Name"), max_length=255, null=True, blank=True)
    accout_type = models.CharField(choices=choices, max_length=15, default="regular")
    avata = models.ImageField(upload_to="profile", null=True, blank=True, default="")
    slug =  models.SlugField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.nickname:
            self.slug = slugify(self.nickname)
        else:
           self.slug = slugify(f"{self.first_name} {self.last_name}")

        return super().save(*args,**kwargs)
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def image_url(self):
        try:
            return self.avata.url
        except:
            return ""
    
