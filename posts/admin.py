from django.contrib import admin
from .models import Profile,Comment,Image

# Register your models here.
admin.site.register(Profile)
admin.site.register(Image)
# admin.site.register(Like)
admin.site.register(Comment)
# admin.site.register(DisLike)
