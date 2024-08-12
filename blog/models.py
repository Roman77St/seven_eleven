from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):

    title = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.SlugField(max_length=250, blank=True, verbose_name='Слаг', unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name='автор')
    body = models.TextField(verbose_name='Текст')
    image = models.ImageField(upload_to='media/blog', blank=True, verbose_name='Изображение')
    publish = models.DateTimeField(default=timezone.localtime, verbose_name='Опубликовано')
    created = models.DateField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    DRAFT = 'DF'
    PUBLISHED = 'PB'
    PUBLISHED_CHOICES = [(DRAFT, 'Черновик'), (PUBLISHED, 'Опубликовано')]
    status = models.CharField(max_length=2, choices=PUBLISHED_CHOICES, default=DRAFT, verbose_name='Статус')

    class Meta:
        db_table = 'post'
        verbose_name='Пост'
        verbose_name_plural='Посты'
        ordering = ['-publish']

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={'slug': self.slug})
    

    def __str__(self) -> str:
        return f'{self.title}'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='пост')
    name = models.CharField(max_length=80, verbose_name='Имя')
    body = models.TextField(verbose_name='Комментарий')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    active = models.BooleanField(default=True, verbose_name='активно')
    class Meta:
        db_table = 'comment'
        verbose_name = 'комментарий'
        verbose_name_plural='Комментарии'
        ordering = ['created']

    def __str__(self) -> str:
        return f'Комментарий {self.name} на пост {self.post}'