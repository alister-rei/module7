from django.shortcuts import render
from rest_framework import generics

from lessons.models import Lesson
from lessons.serializers import LessonSerializer


class LessonCreateAPIView(generics.CreateAPIView):
    """отвечает за создание сущности."""
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    """отвечает за отображение списка сущностей."""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """отвечает за отображение одной сущности."""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonUpdateAPIView(generics.UpdateAPIView):
    """отвечает за редактирование сущности."""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDestroyAPIView(generics.DestroyAPIView):
    """отвечает за удаление сущности."""
    queryset = Lesson.objects.all()
