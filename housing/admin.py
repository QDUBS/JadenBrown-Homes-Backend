from django.contrib import admin

from .models import Address, Images, Category,HouseType, Features, House

admin.site.register((Address, Images, Category,HouseType, Features, House,))