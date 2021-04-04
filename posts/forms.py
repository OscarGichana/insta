from django import forms
from .models import Comment,Profile,Image
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from django.db import models

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['editor', 'active', 'image']
        



class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['editor', 'likes', 'comment',]
    



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','likes','pic')


