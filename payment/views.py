from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from main.paginators import UserPaginator
from payment.models import Payment
from payment.serializers import PaymentSerializer, PaymentCreateSerializer
from users.permissions import IsStaff, OwnerOrModerator


class PaymentCreateAPIView(generics.CreateAPIView):
    """отвечает за создание сущности."""
    serializer_class = PaymentCreateSerializer
    permission_classes = [IsStaff]


class PaymentListAPIView(generics.ListAPIView):
    """отвечает за отображение списка сущностей."""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsStaff]
    pagination_class = UserPaginator

    filter_backends = [DjangoFilterBackend, OrderingFilter]  # Бэкенд для обработки фильтра
    filterset_fields = ('course_pay', 'lesson_pay', 'payment_method')  # Набор полей для фильтрации
    ordering_fields = ('date_payment',)
    # менять порядок сортировки по дате оплаты,


class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    """отвечает за отображение одной сущности."""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsStaff]


class PaymentUpdateAPIView(generics.UpdateAPIView):
    """отвечает за редактирование сущности."""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsStaff]


class PaymentDestroyAPIView(generics.DestroyAPIView):
    """отвечает за удаление сущности."""
    queryset = Payment.objects.all()
    permission_classes = [IsStaff]
