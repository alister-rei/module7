from django.urls import path
from rest_framework import routers

from courses.apps import CoursesConfig
from courses.views import CourseViewSet

app_name = CoursesConfig.name

router = routers.DefaultRouter()
router.register(r'', CourseViewSet)

urlpatterns = [

              ] + router.urls
