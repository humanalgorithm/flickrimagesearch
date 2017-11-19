from rest_framework import serializers
from cache_image.models import CacheImage

class CacheImageIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = CacheImage
        fields = ('id',)


class CacheImageSerializer(serializers.ModelSerializer):
    data = serializers.SerializerMethodField()
    class Meta:
        model = CacheImage
        fields = ('data',)

    def get_data(self, obj):
        return obj.get_data()