from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.forms import BlogForm



class Blog(ListView):
    models = Blog
    queryset  = Blog.objects.all()


class BlogCreate(CreateView):
    models = Blog
    form_class = BlogForm
    success_url = '/blog'