from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('', Blog.as_view(), name='blog'),
    path('blog-create/',BlogCreate.as_view()),
]
