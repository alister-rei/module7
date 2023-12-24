from django.db import models

from django.conf import settings
from rest_framework.exceptions import ValidationError

from courses.models import Course

NULLABLE = {'blank': True, 'null': True}


class Sub(models.Model):
    is_active = models.BooleanField(default=True, verbose_name='активна')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.user} : {self.course} : {self.is_active}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
        unique_together = ('user', 'course')
