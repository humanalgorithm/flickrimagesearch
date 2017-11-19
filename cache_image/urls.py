from django.conf.urls import url
from cache_image.views import CacheImageView
urlpatterns = [
    url(r'^images/$', CacheImageView.as_view()),
]
