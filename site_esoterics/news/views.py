from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import *



def get_news(request):

    posts = News.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
    }

    return render(request, 'news/get_news_2.html', context=context)


# def show_post(request, post_id):
#     return render(request, 'news/get_news_id.html', post_id=post_id)
#     # return HttpResponse(f"Новость с номером id {post_id}")


def show_post(request, post_id):
    post = News.objects.filter(id=post_id)

    context = {
        'post': post,
    }

    return render(request, 'news/get_news_id.html', context=context)