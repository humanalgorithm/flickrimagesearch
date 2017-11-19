
var deleteselected = -1;

$(document).keypress(function(e) {
    if(e.which == 13) {
        getphotolist();
    }
});


var FlickrPhotoService = {
    loadPhotosFromFlickr: function(){

    this._setLoadingIcon()
    flickr_image_id_map = this._makePhotoListRequest(this._loadPhotosById)
    },
    _setLoadingIcon: function(){
        $("#photo-list").text("");
        $("#photo-list").append("<img id='time' src='/static/ajax-loader.gif'/>");
    },

    _makePhotoListRequest(callback){
        self = this
        var search_text = $("#search-text").val();
        var url = "/flickr_request/getphotolist";
        $.ajax({
           type: "GET", url: url, data: {search_text: search_text,},
           success: function(data)
           {
            var flickr_image_id_map = data.flickr_image_id_map;
            if (flickr_image_id_map=='')
            {
              $("#photo-list").text("No results were found");
              return;
            }
            else
            {
              callback(flickr_image_id_map, self)
            }
           },
           error: function (data)
           {}
         });
    },
    _loadPhotosById: function(flickr_image_id_map, self)
    {
      var single_photo_url = "/flickr_request/getsinglephoto";
      for (var key in flickr_image_id_map)
        {
         $.ajax({
             type: "GET",
             url: single_photo_url,
             data: {photo_id: flickr_image_id_map[key],},
             success: function(single_photo_data)
              {
                self._setSinglePhotoImg(single_photo_data)
              },
              error: function(data){}
             });
         }
      self._clearLoadingIcon()
    },
    _setSinglePhotoImg: function(single_photo_data){
      $("#photo-list").append
           (
            "<a class = 'listphotos' href =  \"javascript:updateimagesavefield(\'" + single_photo_data.img_url + "\')\">" +
            "<img src ='" + single_photo_data.img_url + "'>" +
             "</a>"
           );
    },
    _clearLoadingIcon: function(){
      $("#time").text("");
    }

}
