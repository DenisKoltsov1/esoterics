from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *



class CategoryListView(ListView):
    model = News


class CategoryDetailView(DetailView):
    model = News



