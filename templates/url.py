from django.urls import path
from django.conf import settings
from . import views

if settings.DEBUG:
    urlpatterns = [
        path("accont-verification", views.verification_template),
        path('reset-template', views.reset_template)
    ]