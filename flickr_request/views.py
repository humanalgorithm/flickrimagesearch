import simplejson
import urllib2
from django.views.generic.base import View
from django.shortcuts import HttpResponse
from flickr_url import FlickrUrlGenerator


class FlickrImagesListView(View):
    def get(self, request):
        search_text = request.GET.get("search_text")
        try:
            flickr_get_photos_url = FlickrUrlGenerator().get_photos_list_url(search_text)
            page = urllib2.urlopen(flickr_get_photos_url).read()
            photo_data = simplejson.loads(page)
            flickr_image_id_map = {}

            for x in range(0, len(photo_data["photos"]["photo"])):
                flickr_image_id_map[x] = photo_data["photos"]["photo"][x]["id"]

            photo_data_response = simplejson.dumps({"flickr_image_id_map": flickr_image_id_map})
            return HttpResponse(photo_data_response, content_type='application/json')

        except Exception:
            photo_data_response = simplejson.dumps({"flickr_image_id_map": ""})
            return HttpResponse(photo_data_response, content_type='application/json')


class FlickrSingleImageView(View):
    def get(self, request):
        photo_id = request.GET.get('photoid')
        try:
            flickr_single_photo_url = FlickrUrlGenerator().get_single_photo_url(photo_id)
            page = urllib2.urlopen(flickr_single_photo_url).read()
            photo_data_json = simplejson.loads(page)

            single_photo_source = photo_data_json["sizes"]["size"][1]["source"]
            photo_data_response = simplejson.dumps({"singlephotodata": single_photo_source})
            return HttpResponse(photo_data_response, content_type='application/json')
        except Exception:
            photo_data_response = simplejson.dumps({"singlephotodata": ""})
            return HttpResponse(photo_data_response, content_type='application/json')
