
var cacheImageService = {
    saveImage: function(){
      self = this
      callback = self.loadCacheImages
      csrf_token = self._getCsrfToken()
      var image_src = $("#image-save-field").val();
      var url = "/cache_image/images/"
      $.ajax
        ({
          type: "POST",
          url: url,
          data: {
              "image_src_url": image_src,
              "csrfmiddlewaretoken": csrf_token,
            },
            success: function(data)
            {
              callback(self);
            },
            error:
            {  }
        });
    },
    deleteImage: function()
    {
      cache_image_id = this._getDeleteImageCacheId()
      self = this
      var url = "/cache_image/images/" + cache_image_id +"/"
        $.ajax
            ({
              type: "DELETE",
              url: url,
              success: function(data)
               {
                self.loadCacheImages(self);
                $("#delete-image-field").val("");
               },
               error: function(data)
               { }
             });
    },
    loadCacheImages: function(self)
    {
      var cleared = false;
      var url = "/cache_image/images";
      callback = self._setCacheImagesDisplay
      $.ajax({
           type: "GET", url: url,
           data: {},
           success: function(data)
           {
             self._clearCacheImages()
             callback(data)
           },
          error: function(data)
          { }
       });
    },
    _getCsrfToken: function () {
        return document.getElementById('token').getElementsByTagName("input")[0].value
    },
    _getDeleteImageCacheId: function(){
       return $("#delete-image-field").text();
    },
    _setLoadingIcon: function(){
      $("#cache-images").text("");
      $("#cache-images").append("<img id='time' src='/static/ajax-loader.gif'/>");
    },
    _clearCacheImages: function(){
       $("#cache-images").text("");
    },
    _setCacheImagesDisplay: function(cache_image_ids){
      for (i in cache_image_ids)
        {
          $("#cache-images").append(
             "<a class = 'image-selected' href =  \"javascript:updateImageFieldHelper.updateDeleteImageField(\'" + cache_image_ids[i]['id'] + "\')\">" +
             "<img src = '/cache_image/images/" + cache_image_ids[i]['id'] + "'/>" +
             "</a>"
           );
        }
    }
}

var updateImageFieldHelper = {
  updateSaveImageField: function(image_src)
    {
     $("#image-save-field").val(image_src);
    },
  updateDeleteImageField: function(delete_image_id)
    {
      url = "/cache_images/images/" + delete_image_id
      $("#delete-image-field").val(url);
      $("#delete-image-field").text(delete_image_id);
    }
}

