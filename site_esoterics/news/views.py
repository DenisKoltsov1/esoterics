from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *



def get_news(request):
    posts = News.objects.all()
    if len(posts) == 0:
        raise Http404()
    context = {
        'posts': posts,
    }
    return render(request, 'news/get_news_2.html', context=context)


def show_post(request, post_id):
    post = News.objects.filter(id=post_id)
    context = {
        'post': post,
    }
    return render(request, 'news/get_news_id.html', context=context)


# class CategoryListView(ListView):
#     model = News



