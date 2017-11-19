from rest_framework.serializers import ModelSerializer
from cache_image.models import CacheImage

class CacheImageIdSerializer(ModelSerializer):
    class Meta:
        model = CacheImage
        fields = ('id')