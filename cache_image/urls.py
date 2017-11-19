from django.conf.urls import url
from cache_image.views import CacheImageView
from rest_framework import routers
urlpatterns = [
]

router = routers.SimpleRouter()
router.register(r'images', CacheImageView)
urlpatterns += router.urls

print urlpatterns