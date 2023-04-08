from django.shortcuts import render
from .models import Blog


def get_blog(request):
    blog = Blog.objects.all()
    context = {
        'title': 'Ваш профиль',
    }
    return render(request, 'blog/get_blog.html', context)
