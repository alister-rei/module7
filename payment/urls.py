from django.urls import path

from payment.apps import PaymentConfig
from payment.views import PaymentCreateAPIView, PaymentListAPIView, PaymentRetrieveAPIView, PaymentUpdateAPIView, \
    PaymentDestroyAPIView

app_name = PaymentConfig.name

urlpatterns = [
    path('create/', PaymentCreateAPIView.as_view(), name='create'),
    path('', PaymentListAPIView.as_view(), name='list'),
    path('<int:pk>/', PaymentRetrieveAPIView.as_view(), name='view'),
    path('edit/<int:pk>/', PaymentUpdateAPIView.as_view(), name='edit'),
    path('delete/<int:pk>/', PaymentDestroyAPIView.as_view(), name='delete'),
]
