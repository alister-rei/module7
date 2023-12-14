from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=250, verbose_name='название')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(upload_to='couses/', verbose_name='превью (картинка)', **NULLABLE)

    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='владелец', **NULLABLE,
    #                           related_name='owner')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        # ordering = ('titile',)  # сортировка
