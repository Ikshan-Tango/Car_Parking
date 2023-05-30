from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from . import views
from . import models

urlpatterns = [
    path('', views.ApiOverview.as_view(), name="api-overview"),
    path('parkCount/<int:pk>', views.ParkingDetection.as_view(), name="api-overview"),
    path('user-register/',views.Register.as_view(),name = 'user-register'),
    path('user-sigin/',views.SignIn.as_view(),name='user-sigin'),
    path('checkJWT',view=views.HomeView.as_view(),name='hello'),
    path('logout/', views.LogoutView.as_view(), name ='logout')
]
