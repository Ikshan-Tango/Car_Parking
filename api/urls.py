from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from . import views
from . import models

urlpatterns = [
    path('', views.ApiOverview.as_view(), name="api-overview"),
    path('parkCount/<int:pk>', views.ParkingDetection.as_view(), name="api-overview"),
    path('user-register/',views.Register.as_view(),name = 'user-register'),
    path('user-sigin/',views.SignIn.as_view(),name='user-sigin'),
    #token urls
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
