from django.urls import path, include
from rest_framework import routers

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView

app_name = UsersConfig.name

urlpatterns = [
                  path('create/', UserCreateAPIView.as_view(), name='create'),
                  path('', UserListAPIView.as_view(), name='list'),
                  path('<int:pk>/', UserRetrieveAPIView.as_view(), name='view'),
                  path('edit/<int:pk>/', UserUpdateAPIView.as_view(), name='edit'),
                  path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='delete'),
              ]
