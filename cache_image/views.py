import io
import imghdr
import urllib
from cache_image.models import CacheImage
from cache_image.serializers import CacheImageIdSerializer, CacheImageSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from django.shortcuts import HttpResponse

class CacheImageView(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, ListModelMixin, GenericViewSet):
    queryset = CacheImage.objects.all()

    def _getmimetype(self, image):
        mimetype = imghdr.what(io.BytesIO(image.data))
        mime_return = "image/"+mimetype
        return mime_return

    def get_serializer_class(self):
        if self.action == "list":
            return CacheImageIdSerializer
        elif self.action == "retrieve":
            return CacheImageSerializer
        else:
            return CacheImageIdSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return HttpResponse(serializer.data['data'], content_type=self._getmimetype(instance))

    def create(self, request, *args, **kwargs):
        image_src_url = request.POST.get('image_src_url')
        photo = io.BytesIO(urllib.urlopen(image_src_url).read())
        reading = True
        bytesobject = photo.read(4)
        while reading:
            bytes = photo.read(4)
            if (bytes != ""):
                bytesobject = bytesobject + bytes
            else:
                reading = False
                break

        if reading == False:
            try:
                image = CacheImage()
                image.set_data(bytesobject)
                image.save()

                return Response(data={"id": image.id}, status=status.HTTP_201_CREATED)
            except Exception, e:
                return Response(data={"result": "error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

