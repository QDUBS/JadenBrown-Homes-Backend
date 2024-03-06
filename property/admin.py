from django.contrib import admin

from property.models import Images, Property

admin.site.register((Images, Property))