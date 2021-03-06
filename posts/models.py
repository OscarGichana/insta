from django.db import models
import datetime as dt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.dispatch import receiver
from django.db.models.signals import (post_save,pre_save,)
from PIL import Image
from django.core.files import File
from django.dispatch import receiver
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 60,null=True,blank=True)
    last_name = models.CharField(max_length = 60,null=True,blank=True)
    pic = CloudinaryField('pic',null=True) 
    bio = models.TextField(null=True,blank=True)
    likes = models.IntegerField(default=0)
    
    

    def get_total_likes(self):
        return self.likes.user.count()


    def __str__(self):
        return str(self.user.username)
    class Meta:
        ordering = ['first_name']
    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()


def create_profile(sender, instance, created, **kwargs):
    if created: Profile.objects.create(user=instance)

post_save.connect(create_profile, sender = User)


# @receiver(pre_save, sender = Profile)
# def resize_image(sender, instance,**kwargs):
#     max_size = (400, 400)
#     image = Image.open(instance.image)
#     image.thumbnail(max_size)
#     image.save('image.jpg')
#     instance.pic = File(open('image.jpg', 'rb'))
    # class Meta:
    #     ordering = ['first_name']
    # def save_profile(self):
    #     self.save()
    # def delete_profile(self):
    #     self.delete()

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()



class IpModel(models.Model):
    Ip = models.CharField(max_length=100)

    def __str__(self):
        return self.Ip


from tinymce.models import HTMLField

class Image(models.Model):
    name = models.CharField(max_length = 60)
    pic = CloudinaryField('pic',null=True) 
    caption = models.TextField()
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    likes = models.IntegerField(default=0)
    editor = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    # comment = models.ForeignKey(Comment,on_delete=models.CASCADE,null=True)
    # dislikes = models.ForeignKey('Dislike',on_delete=models.CASCADE,null=True)

    @classmethod
    def search_by_name(cls,search_term):
        posts = cls.objects.filter(title__icontains=search_term)
        return posts


    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id, caption):
        update = cls.objects.filter(id = id).update(caption = caption)
        # return update

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id= id).all()
        return image

    
    def get_total_likes(self):
        return self.likes.users.count()

    def __str__(self):
        return str(self.comment)[:30]


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Comment(models.Model):
    image = models.ForeignKey(Image,on_delete=models.CASCADE,related_name='comments',null=True)
    name = models.CharField(max_length=80,null=True)
    email = models.EmailField(null=True)
    body = models.TextField(null=True)
    # created_on = models.DateTimeField(auto_now_add=True,null=True)
    active = models.BooleanField(default=False)
    editor = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    class Meta:
        ordering = ['name']
    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
    


# class Like(models.Model):
#     ''' like  comment '''

#     pic = models.OneToOneField(Image, related_name="likes", on_delete=models.CASCADE)
#     profile = models.ManyToManyField(Profile, related_name='requirement_comment_likes')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return str(self.comment.comment)[:30]

# class DisLike(models.Model):
#     ''' Dislike  comment '''

#     pic = models.OneToOneField(Image, related_name="dis_likes", on_delete=models.CASCADE)
#     profile = models.ManyToManyField(Profile, related_name='requirement_comment_dis_likes')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)