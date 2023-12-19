from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from courses.models import Course
from courses.serializers import CourseSerializer
from main.services import is_member
from users.permissions import OwnerOrModerator, IsOwner, NotModerator


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated, NotModerator]
        elif self.action == 'update':
            permission_classes = [IsAuthenticated, OwnerOrModerator]
        elif self.action == 'delete':
            permission_classes = [IsAuthenticated, IsOwner]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        # Возвращает только объекты, принадлежащие текущему пользователю
        if is_member(self.request.user):
            return self.queryset.all()
        return self.queryset.filter(owner=self.request.user)
