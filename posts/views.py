
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

@login_required(login_url='/accounts/login/')
def profile(request):
    title = 'O_world'
    user = request.user
    return render(request, 'profile.html')

@login_required(login_url='/accounts/login/')
def post_detail(request, year, month, day, image):
    image = get_object_or_404(Image, slug=image,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)

    # List of active comments for this post
    comments = image.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet          
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.image = image
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()                   
    return render(request,'new_comment.html',{'image': image,'comments': comments,'new_comment': new_comment,'comment_form': comment_form})





@login_required(login_url='/accounts/login/')
def like(request, id):
    image = Image.objects.get(id=id)
    image.likes += 1
    image.save()
    return HttpResponseRedirect(reverse("ftPic"))


@login_required(login_url='/accounts/login/')
def follow(request, id):
    profile = Profile.objects.get(id=id)
    profile.likes += 1
    profile.save()
    return HttpResponseRedirect(reverse("profile"))

