from django.urls import path

from property.views import ListPropertyView, PropertyByMangerView, PropertyDetailView, PropertySeachView

urlpatterns = [
    path("", ListPropertyView.as_view(), name="properties"),
    path("search", PropertySeachView.as_view(), name="search"),
    path("detail/<slug:slug>", PropertyDetailView.as_view(), name="property-detail"),
    path("<str:username>/properties", PropertyByMangerView.as_view()),
]