from django.urls import path
from .views import *

urlpatterns = [
    path('', PriceListView.as_view(), name='price_view'),
    path('price-detail/<int:pk>/', PriceDetailView.as_view(), name='price_detail'),
    path('price-create/', PriceCreateView.as_view(), name='price_create'),
    path('price-update/<int:pk>/', PriceUpdateView.as_view(), name='price_update'),
    path('Price-delete/<int:pk>/', PriceDeleteView.as_view(), name='price_delete'),
]