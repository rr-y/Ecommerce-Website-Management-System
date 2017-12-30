from django.conf.urls import url
from . import views

app_name = 'music'
urlpatterns = [
	#/music/

    url(r'^$', views.indexView.as_view(), name ='index'),

    #/music/<album_id>/

    url(r'^(?P<pk>[0-9]+)/$', views.detailView.as_view(), name='detail'),

    # /music/<album_id>/favourite/

    #url(r'^(?P<album_id>[0-9]+)/favourite/$', views1.favourite, name='favourite'),


    #  /music/album/add/

    url(r'album/add/$',views.AlbumCreate.as_view(),name = 'album-add'),

    #  /music/album/2/

    url(r'^register/$', views.UserformView.as_view(), name='register'),


]
