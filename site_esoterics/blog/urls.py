from django.urls import path
from .views import *

urlpatterns = [
    path('', Blog.as_view(), name='blog'),
    path('blog-create/',BlogCreate.as_view(),name='blog_create'),
]
