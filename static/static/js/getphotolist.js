var deleteselected = -1;

$(document).keypress(function(e) {
    if(e.which == 13) {
        getphotolist();
    }
});

function getphotolist()
{
    var cleared = false;
    $("#photolist").text("");
    $("#photolist").append("<img id='time' src='/static/ajax-loader.gif'/>");
    var searchstring = $("#searchstring").val();
    var url = "/getphotolist";

    $.ajax({
           type: "GET", url: url, data: {searchstring: searchstring,},
           success: function(data)
           {
            var response = JSON.parse(data);
            var mapofpicids = response.mapofpicids;

            if (mapofpicids=='')
            {$("#photolist").text("No results were found"); return;}

             getphotos(mapofpicids, cleared);
           },
           error: function (data)
           {}
         });
 }

function getphotos(mapofpicids, cleared)
{
  var urlgetsinglephoto = "/getsinglephoto";
  for (var key in mapofpicids)
            {
             $.ajax
              ({type: "GET", url: urlgetsinglephoto, data: {photoid: mapofpicids[key],},
               success: function(singlephotodata)
                 {
                  if (cleared==false)
                  {$("#photolist").text(""); cleared = true;}
                  $("#photolist").append
                  (
                  "<a class = 'listphotos' href =  \"javascript:updateimagesavefield(\'" + singlephotodata.singlephotodata + "\')\">" +
                  "<img src ='" + singlephotodata.singlephotodata + "'>" +
                  "</a>");
                 },
                 error: function(data)
                {      }
               });
            }
}

function saveimage()
{
 var imagesrc = $("#imagesavefield").val();
 var url = "/imagesavedb/?imagesrc=" + imagesrc;
   $.ajax
           ({
              type: "GET", url: url,
               success: function(data)
                 {
                   loaddbimages();
                 },
                 error:
                 {  }
            });
}
function updateimagesavefield(imagesrc)
{
 $("#imagesavefield").val(imagesrc);
}

function loaddbimages()
{
var cleared = false;
    $("#databaseimages").text("");
    $("#databaseimages").append("<img id='time' src='/static/ajax-loader.gif'/>");
    var url = "/getdbimagelist";
    $.ajax({
           type: "GET", url: url,
           data: {},
           success: function(data)
           {
             var response = JSON.parse(data);
             var dbimageids = response.dbimageids;
             $("#databaseimages").text("");
             for (i in dbimageids)
            {
             $("#databaseimages").append(
                "<a title = '/getsingledbimage/?dbimageid=" + dbimageids[i] + "'class ='imageselected' id='" + dbimageids[i] + "'>"   +   //href = \"javascript:updatedeleteimagefield(" + dbimageids[i] + ")\"
                "<img src = '/getsingledbimage/?dbimageid=" + dbimageids[i] + "'/>" +
                "</a>"
                );
            }
           },
          error: function(data)
          {     }
       });
}

function deleteimage()
{
dbimageid = deleteselected;
var url = "/deleteimage"
    $.ajax
        ({
          type: "GET", url: url, data:{ dbimageid: dbimageid,},
           success: function(data)
           {
            loaddbimages();
            $("#deleteimagefield").val("");
           },
           error: function(data)
           { }
         });
}

function updatedeleteimagefield(dbimagesrc)
{
  $("#deleteimagefield").val(dbimagesrc);
}

$(document).ready(function()
{
loaddbimages();

$('#rightbar').on('click', 'a', function()
  {
    $('.imageselected').each(function() {
    $(this).css("opacity", "1");
     });

    $(this).css("opacity", ".3");

     updatedeleteimagefield($(this).attr('title'));
     deleteselected =  $(this).attr('id');
   });

$('#photolist ').on('click', 'a', function()
    {
    //window.alert( $(this).attr('id') );
    $('.listphotos').each(function() {
    $(this).css("opacity", "1");
     });

    $(this).css("opacity", ".3");

     });

});
