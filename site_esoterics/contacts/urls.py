from django.urls import path
from .views import *
from . import views
urlpatterns = [
     path('', ContactListView.as_view(), name='contact_view'),
     #path('', contact),
     path("postuser/", views.postuser),
]
    