from django.conf.urls import url
from page import views

urlpatterns = [
               url(r'^$', views.index, name="index"),
               url(r'^.*/$', views.fourzerofour, name="fourzerofour"),
               ]
