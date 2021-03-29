from django.shortcuts import render, redirect
from django.http  import HttpResponse
import datetime as dt
from django.http  import HttpResponse,Http404
from .models import Comment,Image,Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django import forms
from .forms import CommentForm
from django.contrib.auth import authenticate,logout,login

# Create your views here.
def index(request):
    images = Image.get_all_images()
    title = 'O_world'
    return render(request, 'index.html', {"images":images})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except Image.DoesNotExist:
        raise Http404()
    return render(request,"index.html", {"image":image})



def new_comment(request):
    # current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            # comment.editor = current_user
            comment.save()
        return redirect('ftPic')

    else:
        form = CommentForm()
    return render(request, 'new_comment.html', {"form": form})



      
class UpdateCommentVote(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, request, *args, **kwargs):

        comment_id = self.kwargs.get('comment_id', None)
        opinion = self.kwargs.get('opinion', None) # like or dislike button clicked

        comment = get_object_or_404(models.Comment, id=comment_id)

        try:
            # If child DisLike model doesnot exit then create
            comment.dis_likes
        except models.Comment.dis_likes.RelatedObjectDoesNotExist as identifier:
            vtu_models.DisLike.objects.create(comment = comment)

        try:
            # If child Like model doesnot exit then create
            comment.likes
        except vtu_models.Comment.likes.RelatedObjectDoesNotExist as identifier:
            models.Like.objects.create(comment = comment)

        if opition.lower() == 'like':

            if request.user in comment.likes.users.all():
                comment.likes.users.remove(request.user)
            else:    
                comment.likes.users.add(request.user)
                comment.dis_likes.users.remove(request.user)

        elif opition.lower() == 'dis_like':

            if request.user in comment.dis_likes.users.all():
                comment.dis_likes.users.remove(request.user)
            else:    
                comment.dis_likes.users.add(request.user)
                comment.likes.users.remove(request.user)
        else:
            return HttpResponseRedirect(reverse('comment'))
        return HttpResponseRedirect(reverse('comment'))
