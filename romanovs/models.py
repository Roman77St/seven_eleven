from django.db import models

class Tsar(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    patronymic = models.CharField(max_length=100, null=True, blank=True, verbose_name='Отчество')
    image = models.ImageField(upload_to='media/romanovs', verbose_name='Изображение')
    period_of_goverment = models.CharField(max_length=200, verbose_name='Период правления')
    slug = models.SlugField(max_length=200, null=True, blank=True, unique=True,verbose_name='Слаг')

    class Meta:
        db_table = 'romanovs'
        verbose_name = 'Царь'
        verbose_name_plural = 'Цари'

    def __str__(self) -> str:
        return f'{self.name}'