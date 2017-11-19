






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

