
var deleteselected = -1;

$(document).keypress(function(e) {
    if(e.which == 13) {
        getphotolist();
    }
});


var FlickrPhotoService = {
    loadPhotosFromFlickr: function(){

    this._setLoadingIcon()
    flickr_image_id_map = this._makePhotoListRequest()

    },
    _setLoadingIcon: function(){
        $("#photo-list").text("");
        $("#photo-list").append("<img id='time' src='/static/ajax-loader.gif'/>");
    },

    _makePhotoListRequest(){
        var search_text = $("#search-text").val();
        var url = "/getphotolist";
        $.ajax({
           type: "GET", url: url, data: {search_text: search_text,},
           success: function(data)
           {
            var response = JSON.parse(data);
            var flickr_image_id_map = response.flickr_image_id_map;

            if (flickr_image_id_map=='')
            {
              $("#photo-list").text("No results were found");
              return;
            }
            else
            {
              return flickr_image_id_map
            }
           },
           error: function (data)
           {}
         });
    },

    _loadPhotosById: function getphotos(flickr_image_id_map)
    {
      var single_photo_url = "/getsinglephoto";
      for (var key in flickr_image_id_map)
        {
         $.ajax({
             type: "GET", 
             url: urlgetsinglephoto,
             data: {photo_id: flickr_image_id_map[key],},
             success: function(singlephotodata)
              {

              },
              error: function(data){}
             });
         }
    },
    _setSinglePhotoImg: function(){
      $("#photo-list").append
           (
            "<a class = 'listphotos' href =  \"javascript:updateimagesavefield(\'" + singlephotodata.singlephotodata + "\')\">" +
            "<img src ='" + singlephotodata.singlephotodata + "'>" +
             "</a>"
           );
    }

}
