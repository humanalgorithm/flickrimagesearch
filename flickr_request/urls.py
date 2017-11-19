from django.conf.urls import url
from flickr_request.views import FlickrImagesListView, FlickrSingleImageView


urlpatterns = [
    url(r'^getphotolist/$', FlickrImagesListView.as_view()),
    url(r'^getsinglephoto/$', FlickrImagesListView.as_view()),
]
