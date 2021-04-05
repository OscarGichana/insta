"""gram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views 
# from django.urls import path


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('posts.urls')),
    url(r'^accounts/', include('django_registration.backends.simple.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    url(r'^logout/$', views.LogoutView.as_view()),
    url(r'members/', include('django.contrib.auth.urls')),
    url(r'members',include('members.urls')),
    url(r'^tinymce/', include('tinymce.urls')),


]
