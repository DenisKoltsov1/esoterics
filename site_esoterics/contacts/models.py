from django.db import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    sname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
