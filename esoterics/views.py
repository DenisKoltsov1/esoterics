from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template import RequestContext




def index(request):
  
    return render(request, 'esoterics/index.html')