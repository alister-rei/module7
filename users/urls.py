from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create/', UserCreateAPIView.as_view(), name='create'),
    path('', UserListAPIView.as_view(), name='list'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='view'),
    path('edit/<int:pk>/', UserUpdateAPIView.as_view(), name='edit'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='delete'),
]
