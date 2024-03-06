from django.urls import path

from account.views import AccountProfileView


urlpatterns = [
    path("", AccountProfileView.as_view(), name="user_profile"),
]