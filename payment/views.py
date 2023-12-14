from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from payment.models import Payment
from payment.serializers import PaymentSerializer, PaymentCreateSerializer


class PaymentCreateAPIView(generics.CreateAPIView):
    """отвечает за создание сущности."""
    serializer_class = PaymentCreateSerializer


class PaymentListAPIView(generics.ListAPIView):
    """отвечает за отображение списка сущностей."""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter]  # Бэкенд для обработки фильтра
    filterset_fields = ('course_pay', 'lesson_pay', 'payment_method')  # Набор полей для фильтрации
    ordering_fields = ('date_payment',)
    # менять порядок сортировки по дате оплаты,

class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    """отвечает за отображение одной сущности."""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentUpdateAPIView(generics.UpdateAPIView):
    """отвечает за редактирование сущности."""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentDestroyAPIView(generics.DestroyAPIView):
    """отвечает за удаление сущности."""
    queryset = Payment.objects.all()