from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.forms import BlogForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.http import HttpResponse
    
import requests

class Blog(ListView):
    models = Blog
    queryset  = Blog.objects.all()

class BlogCreate(UserPassesTestMixin,CreateView):
    models = Blog
    form_class = BlogForm
    success_url = '/blog'
    template_name = 'blog/blog_form.html'
    
    def test_func(self):
        return self.request.user.is_staff

'''

class BlogCreate(UserPassesTestMixin,CreateView):
    models = Blog
    form_class = BlogForm
    success_url = '/blog'
    #template_name = 'path/to/file.html'
    def test_func(self):
        return self.request.user.is_staff
 
   
def CreateBlog(requests):
   
    form = BlogForm(initial=dict(name=requests.name,email=requests.email,specialization=requests.specialization,mobile=requests.mobile,address=requests.adress,photo=requests.photo))
    context = dict(form=form)
    return render(requests, 'blog_form.html',form)
    '''


class BlogDeleteView(UserPassesTestMixin, DeleteView):
    model = Blog
    success_url = '/blog'

    def test_func(self):
        return self.request.user.is_superuser    