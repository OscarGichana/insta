
from django.shortcuts import render,redirect,get_object_or_404,reverse
import datetime as dt
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Comment,Image,Profile,UpdateProfile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, DetailView
from django import forms
from .forms import NewImageForm,NewCommentForm
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from .models import IpModel,Image,Comment

# Create your views here.
def index(request):
    images = Image.get_all_images()
    title = 'O_world'
    return render(request, 'index.html', {"images":images})

