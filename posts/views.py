from django.shortcuts import render, redirect
from django.http  import HttpResponse
import datetime as dt
from django.http  import HttpResponse,Http404
from .models import Post

# Create your views here.
def index(request):
    title = 'O_world'
    return render(request, 'index.html')
