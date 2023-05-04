from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.forms import BlogForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin

class Blog(ListView):
    models = Blog
    queryset  = Blog.objects.all()


class BlogCreate(UserPassesTestMixin,CreateView):
    models = Blog
    form_class = BlogForm
    success_url = '/blog'
    #template_name = 'path/to/file.html'
    def test_func(self):
        return self.request.user.is_staff
    

'''
    class PriceUpdateView(UserPassesTestMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    success_url = '/Price'

    def test_func(self):
        return self.request.user.is_staff
'''

class BlogDeleteView(UserPassesTestMixin, DeleteView):
    model = Blog
    success_url = '/blog'

    def test_func(self):
        return self.request.user.is_superuser    