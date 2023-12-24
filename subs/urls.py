from django.urls import path

from subs.apps import SubsConfig
from subs.views import SubCreateAPIView, SubDestroyAPIView, SubListAPIView

app_name = SubsConfig.name

urlpatterns = [
    path('create/', SubCreateAPIView.as_view(), name='create'),
    path('', SubListAPIView.as_view(), name='list'),
    path('delete/<int:pk>/', SubDestroyAPIView.as_view(), name='delete')
]
