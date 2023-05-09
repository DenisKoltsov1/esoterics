from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.ImageField()
    message = models.TextField(max_length=1000)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Будет отображаться следующее поле в панели администрирования
        return '{} {} {} {} {}'.format(self.name,self.email ,self.phone,self.message,self.time_create)
    



    