from django.shortcuts import render



def get_news(request):
    return render(request, 'news/base_news.html')

