from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from lessons.models import Lesson
from lessons.serializers import LessonSerializer
from main.services import is_member
from users.permissions import OwnerOrModerator, IsOwner, NotModerator


class LessonCreateAPIView(generics.CreateAPIView):
    """отвечает за создание сущности."""
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, NotModerator]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    """отвечает за отображение списка сущностей."""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, OwnerOrModerator]

    def get_queryset(self):
        # Возвращает только объекты, принадлежащие текущему пользователю
        if is_member(self.request.user):
            return self.queryset.all()
        return self.queryset.filter(owner=self.request.user)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """отвечает за отображение одной сущности."""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, OwnerOrModerator]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """отвечает за редактирование сущности."""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, OwnerOrModerator]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """отвечает за удаление сущности."""
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
