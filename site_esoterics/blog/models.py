from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User
class Blog(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(max_length=100,verbose_name='Gmail')
    specialization = models.CharField(max_length=100, verbose_name='Специализация')
    mobile = models.CharField(max_length=100, verbose_name='Телефон')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    photo = models.ImageField(max_length=100,upload_to='user_photo/')
    #created_at = models.DateTimeField(max_length=100,auto_now=True, verbose_name='Дата создания')
    #updated_at = models.DateTimeField(max_length=100,auto_now_add=True, verbose_name='Дата изменения')
    
    
    class Meta:
        verbose_name = 'Блог'
        #verbose_name_plural = 'Пользователи'
        
        
    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.name,self.email ,self.specialization,self.mobile,self.address,self.photo)


    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name_plural = 'Блог'