from django.urls import path

from lessons.apps import LessonsConfig
from lessons.views import LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView

app_name = LessonsConfig.name

urlpatterns = [
    path('create/', LessonCreateAPIView.as_view(), name='create'),
    path('', LessonListAPIView.as_view(), name='list'),
    path('<int:pk>/', LessonRetrieveAPIView.as_view(), name='view'),
    path('edit/<int:pk>/', LessonUpdateAPIView.as_view(), name='edit'),
    path('delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='delete'),
]
