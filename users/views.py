from rest_framework import generics, status
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer, UserCreateSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """отвечает за создание сущности."""
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserListAPIView(generics.ListAPIView):
    """отвечает за отображение списка сущностей."""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """отвечает за отображение одной сущности."""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    """отвечает за редактирование сущности."""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    """отвечает за удаление сущности."""
    queryset = User.objects.all()
