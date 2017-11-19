from django.conf.urls import url
from page import views

urlpatterns = [
               url(r'^index/$', views.index, name="learnmore"),
               url(r'^.*/$', views.fourzerofour, name="fourzerofour"),
               ]
