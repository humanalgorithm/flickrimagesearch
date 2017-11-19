"""newproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



admin.autodiscover()
urlpatterns = [
               url(r'^cache_image/', include('cache_image.urls')),
               url(r'^flickr_request/', include('flickr_request.urls')),
               url(r'', include('page.urls')),
               ]



'''
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'newapp.views.home', name='home'),
    url(r'^getphotolist/', 'newapp.views.getphotolist', name='getphotolist'),
    url(r'^getsinglephoto/', 'newapp.views.getsinglephoto', name='getsinglephoto'),
    url(r'^getdbimages/', 'newapp.views.getdbimages', name='getdbimages'),
    url(r'^getdbimagelist/', 'newapp.views.getdbimagelist', name='getdbimagelist'),
    url(r'^getsingledbimage/', 'newapp.views.getsingledbimage', name='getsingledbimage'),
    url(r'^imagesavedb/', 'newapp.views.imagesavedb', name='imagesavedb'),
    url(r'^deleteimage/', 'newapp.views.deleteimage', name='deleteimage'),
    url(r'^.*/$', 'newapp.views.fourzerofour', name='fourzerofour')
]
'''

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)