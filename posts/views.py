
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

class PostDetailView(DetailView):
    model = Imagecontext_object_name = 'post'
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        like_status = False
        if self.object.likes.filter(id=IpModel.objects.get(Ip=Ip).id).exists():
            like_status = True
        else:
            like_status =False
        context['like_status'] = like_status

        return self.render_to_response(context)


@login_required(login_url='/accounts/login/')

def  get_client_ip(request):
    x_forward_for = request.META.get('HTTP_X_FORWARD_FOR')
    if x_forward_for:
        Ip = x_forward_for.split(',')[0]
    else:
        Ip = request.META.get('REMOTE_ADDR')
    return Ip

@login_required(login_url='/accounts/login/')

def postlike(request, pk):
    global image
    image_id = request.POST.get('blog-id')
    image = Image.objects.filter(pk=image_id)
    Ip = get_client_ip(request)
    if not IpModel.objects.filter(Ip=Ip).exists():
        IpModel.objects.create(Ip=Ip)
        
    if image.likes.filter(id=IpModel.objects.get(Ip=Ip).id).exists():
        image.likes.remove(IpModel.objects.get(Ip=Ip))
    else:
        image.likes.add(IpModel.objects.get(Ip=Ip))

    return HttpResponseRedirect(reverse('blog_like', args=[image_id]))


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

