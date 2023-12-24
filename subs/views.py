from django.shortcuts import render
from rest_framework import generics, serializers
from rest_framework.permissions import IsAuthenticated

from courses.models import Course
from main.paginators import UserPaginator
from subs.models import Sub
from subs.serializers import SubSerializer
from users.permissions import IsStaff, IsOwner


class SubCreateAPIView(generics.CreateAPIView):
    queryset = Sub.objects.all()
    serializer_class = SubSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer, *args, **kwargs):
        user = self.request.user
        course = Course.objects.get(id=self.request.data.get('course'))  # Получаем курс из запроса
        try:
            # Проверяем, существует ли уже подписка на данный курс у пользователя
            sub = Sub.objects.get(user=user, course=course)
        except Sub.DoesNotExist:
            # Если подписки нет, создаем новую и привязываем пользователя
            sub = serializer.save(user=user, course=course)
        else:
            # Если подписка уже существует, можно выбросить исключение или выполнить другую логику
            raise serializers.ValidationError('У вас уже есть подписка на данный курс')


class SubListAPIView(generics.ListAPIView):
    queryset = Sub.objects.all()
    serializer_class = SubSerializer
    permission_classes = [IsStaff]
    pagination_class = UserPaginator


class SubDestroyAPIView(generics.DestroyAPIView):
    queryset = Sub.objects.all()
    serializer_class = SubSerializer
    permission_classes = [IsStaff | IsOwner]
