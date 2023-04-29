from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from rest_framework import generics
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from .serializers import PriceSerialazer
from price.forms import PriceForm


class PriceListView(ListView):
    model = Price
   

class PriceAPIView(generics.ListAPIView):
    queryset = Price.objects.all()
    serealizer_class = PriceSerialazer

class PriceListView(ListView):
    model = Price
    

class PriceDetailView(LoginRequiredMixin, DetailView):
    model = Price


class PriceCreateView(UserPassesTestMixin, CreateView):
    model = Price
    form_class = PriceForm
    success_url = '/price'
    #template_name = 'price-list.html'
    def test_func(self):
        return self.request.user.is_staff


class PriceUpdateView(UserPassesTestMixin, UpdateView):
    model = Price
    form_class = PriceForm
    success_url = '/Price'

    def test_func(self):
        return self.request.user.is_staff


class PriceDeleteView(UserPassesTestMixin, DeleteView):
    model = Price
    success_url = '/Price'

    def test_func(self):
        return self.request.user.is_superuser    
