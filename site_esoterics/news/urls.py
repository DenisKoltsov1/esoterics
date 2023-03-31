from django.contrib import admin
from django.urls import path, include
from django.urls import path
from .views import *



urlpatterns = [
    #path('', get_news, name='get_news'),
    #path('post/<int:post_id>/', show_post, name='post'),
    #CRUD
    path('', CategoryListView.as_view(), name='news_view'),
    path('news-detail/<int:pk>/', CategoryDetailView.as_view(), name='news_detail'),
]
