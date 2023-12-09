from django.conf import settings
from django.db import models

from courses.models import Course

NULLABLE = {'blank': True, 'null': True}


class Lesson(models.Model):
    title = models.CharField(max_length=250, verbose_name='название')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(upload_to='couses/', verbose_name='превью (картинка)', **NULLABLE)
    video = models.URLField(verbose_name='ссылка на видео', **NULLABLE)

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')

    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='владелец', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        # ordering = ('titile',)  # сортировка
