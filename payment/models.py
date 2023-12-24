from django.db import models

from config import settings
from courses.models import Course
from lessons.models import Lesson

NULLABLE = {'blank': True, 'null': True}


class Payment(models.Model):
    CASH = "наличные"
    TRANSFER = "перевод"

    PAYMENT_CHOICE = [(CASH, "наличные"), (TRANSFER, "перевод")]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='пользователь',
                             **NULLABLE,
                             related_name='user')
    date_payment = models.DateTimeField(auto_now_add=True, verbose_name='Дата оплаты')
    lesson_pay = models.ForeignKey(Lesson, **NULLABLE, on_delete=models.SET_NULL, verbose_name='оплаченный  Урок',
                                   related_name='lesson')
    course_pay = models.ForeignKey(Course, **NULLABLE, on_delete=models.SET_NULL, verbose_name='оплаченный  Курс',
                                   related_name='course')
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за покупку')
    payment_method = models.CharField(max_length=25, choices=PAYMENT_CHOICE, verbose_name='способ оплаты')

    def __str__(self):
        return f'{self.user} by {self.lesson_pay if self.lesson_pay else self.course_pay}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
        unique_together = ('user', 'course_pay')
        # ordering = ('date_payment',)  # сортировка
