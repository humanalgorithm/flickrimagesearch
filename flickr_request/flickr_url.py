from django.conf import settings


class FlickrUrlGenerator():
    flickr_base_url  = "https://api.flickr.com/services/rest/"
    json_format = "json&nojsoncallback=1"

    def get_photos_list_url(self, search_text):
        flickr_get_photos_method = "flickr.photos.search"
        url = "{}?method={}&api_key={}&text={}&format={}".format(
            self.flickr_base_url,
            flickr_get_photos_method,
            settings.FLICKR_API_KEY,
            search_text,
            self.json_format)
        return url

    def get_single_photo_url(self, photo_id):
        flickr_get_single_photo_method="flickr.photos.getSizes"
        url = "{}?method={}&api_key={}&photo_id={}&format={}".format(
            self.flickr_base_url,
            flickr_get_single_photo_method,
            settings.FLICKR_API_KEY,
            photo_id,
            self.json_format)
        return url