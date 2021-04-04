from django.conf.urls import url
from . import views 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns=[
    url(r'^$',views.index,name='ftPic'),
    url(r'^new/comment/(?P<image_id>\d+)', views.new_comment, name='new-comment'),
    url(r'^image/(?P<image_id>\d+)',views.single,name = 'single'),
    url(r'^like/(\d+)',views.like,name = 'like'),
    url(r'^profile',views.profile,name = 'profile'),
    url(r'^follow/(\d+)',views.follow,name = 'follow'),
    url(r'^name', views.post_detail, name='post_detail'),
    url(r'^user_profile/(?P<image_id>\d+)',views.user_profile,name = 'user_profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^new/image$', views.new_image, name='new-image')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


