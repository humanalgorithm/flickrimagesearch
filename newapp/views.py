from django.shortcuts import render_to_response, RequestContext, HttpResponse
import ioOps
import urllib

def home(request):
        return render_to_response("home.html",
                              locals(),
                              context_instance =RequestContext(request))

def fourzerofour(request):
      return render_to_response("fourzerofour.html",
                              locals(),
                              context_instance =RequestContext(request))

def getdbimagelist(request):
    dbimageids = ioOps.getdbimageids()
    print dbimageids
    return HttpResponse(dbimageids, content_type='application/json')

def getsingledbimage(request):
    try:
        returnimage = ioOps.getdbimage(str(request.GET["dbimageid"]))
        mimetype = ioOps.getmimetype(returnimage)
        return HttpResponse(returnimage.get_data(), content_type="image/" + mimetype)
    except Exception,e:
        print str(e)

def deleteimage(request):
        dbimageid = str(request.GET["dbimageid"])
        result = ioOps.deleteimage(dbimageid)
        return HttpResponse("<h1>Delete returned " + str(result) + "</h1>")

def imagesavedb(request):
    imagesrc = str(request.GET["imagesrc"])
    result = ioOps.saveimagetodb(imagesrc)
    return HttpResponse("<h1>Save returned " + str(result) + "</h1>")

def getphotolist(request):
    try:
        searchstring = str(request.GET["searchstring"])
        searchstringhash = {}
        searchstringhash["text"] = searchstring
        print("search string 0 is " + str(urllib.urlencode(searchstringhash)))
        returndata = ioOps.getphotolist(urllib.urlencode(searchstringhash))
        return HttpResponse(returndata, content_type='application/json')
    except Exception, e:
        print str(e)

def getsinglephoto(request):
      input = str(request.GET["photoid"])
      returndata = ioOps.getsinglephoto(input)
      return HttpResponse(returndata, content_type='application/json')


