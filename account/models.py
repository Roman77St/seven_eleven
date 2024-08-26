from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    date_of_birthday = models.DateField(blank=True, null=True, verbose_name='День рождения')
    photo = models.ImageField(upload_to='media/users', blank=True, verbose_name='фото')
    def __str__(self) -> str:
        return f'Профайл пользователя {self.user.username}'
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
 