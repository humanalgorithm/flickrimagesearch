import simplejson
import io
import imghdr
import urllib
from django.shortcuts import render, HttpResponseRedirect
from rest_framework import generics
from django.views.generic.base import View
from cache_image.models import CacheImage
from rest_framework.viewsets import ModelViewSet
from cache_image.serializers import CacheImageIdSerializer


class CacheImageView(ModelViewSet):
    queryset = CacheImage.objects.all()
    serializer = CacheImageIdSerializer

    def getmimetype(self, returnimage):
        mimetype = imghdr.what(io.BytesIO(returnimage.data))
        return mimetype

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
            # with open('out.jpg', 'wb') as out_file:
            try:
                image = CacheImage()
                image.set_data(bytesobject)
                image.save()
                # out_file.write(bytesobject)
                # out_file.close()
                return True
            except Exception, e:
                return False

    def destroy(self, request, *args, **kwargs):

        super(CacheImageView, self).destroy(*args, **kwargs)
        '''

        try:
            deleteimage = CacheImage.objects.get(id=dbimageid)
            deleteimage.delete()
            return True
        except Exception, e:
            print(str(e))
            return False
        '''

