from django.urls import path

from . import views
from . import models

urlpatterns = [
    path('', views.ApiOverview.as_view(), name="api-overview"),
    path('parkCount/', views.ParkingDetection.as_view(), name="api-overview"),
]
