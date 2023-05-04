from django.urls import path
from .views import *

urlpatterns = [
    path('', ContactListView.as_view(), name='contact_view'),
]
    