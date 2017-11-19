
$(document).ready(function()
{
  self = cacheImageService
  cacheImageService.loadCacheImages(self)
  $('#right-bar').on('click', 'a', function()
    {
      $('.image-selected').each(function()
      {
        $(this).css("opacity", "1");
      });

      $(this).css("opacity", ".3");

   });

  $('#photo-list ').on('click', 'a', function()
     {
       $('.listphotos').each(function()
        {
          $(this).css("opacity", "1");
        });

      $(this).css("opacity", ".3");
     });

});