from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import NewsForm


class NewsListView(ListView):
    model = News


class NewsDetailView(DetailView):
    model = News


class NewsCreateView(CreateView):
    model = News
    form_class = NewsForm
    success_url = '/news'


class NewsUpdateView(UpdateView):
    model = News
    form_class = NewsForm
    success_url = '/news'


class NewsDeleteView(DeleteView):
    model = News
    success_url = '/news'