from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.SlugField(max_length=250, blank=True, verbose_name='Слаг')
    body = models.TextField(verbose_name='Текст')
    image = models.ImageField(upload_to='media/blog', blank=True)
    publish = models.DateTimeField(default=timezone.now, verbose_name='Опубликовано')
    created = models.DateField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    class Meta:
        db_table = 'post'
        verbose_name='Пост'
        verbose_name_plural='Посты'
        ordering = ['-publish']

    def __str__(self) -> str:
        return f'{self.title}'
