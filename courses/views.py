from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from config import settings
from courses.models import Course
from courses.serializers import CourseSerializer
from main.paginators import CoursePaginator
from main.services import mail_sender
from subs.models import Sub
from users.permissions import OwnerOrModerator, IsOwner, NotModerator


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CoursePaginator

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

    # def get_queryset(self):
    #     # Возвращает только объекты, принадлежащие текущему пользователю
    #     if is_member(self.request.user):
    #         return self.queryset.all()
    #     return self.queryset.filter(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save()
        pk = self.kwargs.get('pk')
        course = get_object_or_404(Course, pk=pk)
        subs = Sub.objects.filter(course=course, is_active=True)
        email = list(subs.values_list('user__email', flat=True))  #

        mail_sender(email)
        return Response('Message sent')
