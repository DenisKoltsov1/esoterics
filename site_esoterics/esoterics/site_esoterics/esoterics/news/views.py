from django.shortcuts import render
from django.http import Http404
from .models import *



def get_news(request):

    posts = News.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
    }

    return render(request, 'news/get_news.html', context=context)

