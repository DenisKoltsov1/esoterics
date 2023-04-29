from django.db import models
from django.urls import reverse

class Price(models.Model):
    nameService = models.CharField(max_length=255);
    content = models.TextField(blank=True)
    price = models.IntegerField()



    def __str__(self):
        return self.nameService,self.content,self.price


    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name_plural = 'Новости'