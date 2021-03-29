from django.db import models
import datetime as dt
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)
    pic = models.ImageField(upload_to = 'uploads/')
    bio = models.TextField()

    def __str__(self):
        return self.first_name
    class Meta:
        ordering = ['first_name']
    def save_editor(self):
        self.save()
    def delete_editor(self):
        self.delete()


class Image(models.Model):
    name = models.CharField(max_length = 60)
    pic = models.ImageField(upload_to = 'uploads/')
    caption = models.TextField()
    profile = models.ForeignKey('Profile',on_delete=models.CASCADE,null=True)
    # likes = models.ForeignKey('Like',on_delete=models.CASCADE,null=True)
    # comments = models.ForeignKey('Comment',on_delete=models.CASCADE,null=True)
    # dislikes = models.ForeignKey('Dislike',on_delete=models.CASCADE,null=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id ,name, description , image_location, image_category):
        update = cls.objects.filter(id = id).update(name = name, description = description ,image_location = image_location,image_category = image_category)
        # return update

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id= id).all()
        return image

    @classmethod
    def search_by_category(cls,image_category):
        images = Image.objects.filter(image_category__name__icontains=image_category)
        return images

    @classmethod
    def filter_by_location(cls, image_location):
        images = cls.objects.filter(image_location__name__icontains=image_location)
        return images
    
    def get_total_likes(self):
        return self.likes.users.count()

    def get_total_dis_likes(self):
        return self.dis_likes.users.count()

    def __str__(self):
        return str(self.comment)[:30]


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Comment(models.Model):
    ''' Main comment model'''
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


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

    def __str__(self):
        return str(self.comment.comment)[:30]
