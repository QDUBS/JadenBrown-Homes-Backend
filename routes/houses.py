from django.urls import path
from housing.views import HouseByMangerView, HouseDetailView, HouseListView, ImagesView, SearchHouseView


urlpatterns = [
    path("houses", HouseListView.as_view(), name="house-list"),
    path("houses/search", SearchHouseView.as_view(), name="search-houses"),
    path("images", ImagesView.as_view(), name="images"),
    path("<str:username>/houses", HouseByMangerView.as_view()),
    path("houses/<slug:slug>", HouseDetailView.as_view(), name="house-detail"),

]