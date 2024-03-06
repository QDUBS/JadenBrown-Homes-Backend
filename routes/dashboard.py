from django.urls import path

from housing.views import ManagerHousesDashboardView
from property.views import ManagerPropertyDashboardView

urlpatterns = [
    path("houses", ManagerHousesDashboardView.as_view(), name="dashboard-housing"),
    path("properties", ManagerPropertyDashboardView.as_view(), name="dashboard-property"),
]