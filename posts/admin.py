from django.contrib import admin
from .models import Profile,Comment,Image

# Register your models here.
admin.site.register(Profile)
admin.site.register(Image)
# admin.site.register(Like)
admin.site.register(Comment)
# admin.site.register(DisLike)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'body', 'image', 'active')
    list_filter = ('active', 'name')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
