from django.urls import path

from . import views
from . import models

urlpatterns = [
    path('', views.ApiOverview.as_view(), name="api-overview"),
    path('parkCount/<int:pk>', views.ParkingDetection.as_view(), name="api-overview"),
]
