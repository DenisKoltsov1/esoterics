from django.db import models
from django.core.validators import validate_email, ValidationError
from django.shortcuts import reverse


def email_validations(value):
    try:
        email_validations(value)
    except ValidationError as e:
        return 'Плохой эмэйл'
    else:
        return 'Отлично'


class Blog(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    mail = models.EmailField(verbose_name='Gmail')
    photo = models.ImageField(upload_to='user_photo/')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата изменения')
    info = models.TextField(max_length=500, verbose_name='Краткая информация')
    email = models.EmailField(blank=True, null=True, validators=[email_validations], verbose_name='Эмэйл')
    phone = models.BooleanField(blank=True, null=True, verbose_name='Номер')
    address = models.TextField(blank=True, null=True, verbose_name='Адресс')
    instagram = models.TextField(null=True, blank=True, verbose_name='Соц-сеть Instagram')
    vk = models.TextField(null=True, blank=True, verbose_name='Соц-сеть VK')
    telegram = models.TextField(null=True, blank=True, verbose_name='Соц-сеть Telegram')
    work = models.CharField(max_length=20, blank=True, null=True, verbose_name='Профессия')

    def get_name(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog', kwargs={'bolg_id': self.pk})

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Пользователи'
