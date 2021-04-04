from django.conf.urls import url
from . import views 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns=[
    url(r'^$',views.index,name='ftPic'),
    url(r'^new/comment/(?P<image_id>\d+)', views.new_comment, name='new-comment'),

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


