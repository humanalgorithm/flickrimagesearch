from models import ImageFile
import json
import io
import imghdr
import urllib
import urllib2
import simplejson
import configvars

flickrbaseurl = configvars.flickrbaseurl
flickgetphotosmethod = configvars.flickgetphotosmethod
apikey = configvars.apikey
flickrgetphotomethod= configvars.flickrgetphotomethod
jsonformat = configvars.jsonformat

def getdbimageids():
    dbimageids = []
    for e in ImageFile.objects.all():
        dbimageids.append(e.id)
    returndata = json.dumps({
                "dbimageids": dbimageids,
                  })
    return json.dumps(returndata)


def getdbimage(dbimageid):
        returnimage = ImageFile.objects.get(id=dbimageid)
        return returnimage

def getmimetype(returnimage):
    mimetype = imghdr.what(io.BytesIO(returnimage.data))
    return mimetype


def saveimagetodb(imagesrc):
    photo = io.BytesIO(urllib.urlopen(imagesrc).read())
    reading = True
    bytesobject = photo.read(4)
    while reading:
        bytes = photo.read(4)
        if(bytes !=""):
          bytesobject = bytesobject + bytes
        else:
          reading = False
          break

    if reading ==False:
         #with open('out.jpg', 'wb') as out_file:
        try:
          image = ImageFile()
          image.set_data(bytesobject)
          image.save()
          #out_file.write(bytesobject)
          #out_file.close()
          return True
        except Exception, e:
          return False

def deleteimage(dbimageid):
    try:
      deleteimage = ImageFile.objects.get(id=dbimageid)
      deleteimage.delete()
      return True
    except Exception, e:
        print(str(e))
        return False

def getphotolist(searchstring):
    try:
        urlphotos = flickrbaseurl + flickgetphotosmethod + apikey + "&"+ searchstring + jsonformat
        print urlphotos
        page = urllib2.urlopen(urlphotos).read()
        dataphotolist = simplejson.loads(page)
        mapofpicids = {}
        for x in range(0,len(dataphotolist["photos"]["photo"])):
                mapofpicids[x] = dataphotolist["photos"]["photo"][x]["id"]

        returndata = json.dumps({
        "mapofpicids": mapofpicids,
                })
        return json.dumps(returndata)
    except Exception,e:
        print str(e)
        returndata = json.dumps({
        "mapofpicids": "",
                })
        return json.dumps(returndata)

def getsinglephoto(input):
        urlgetphoto = flickrbaseurl + flickrgetphotomethod + apikey + "&photo_id=" + input + jsonformat
        getphotopage = urllib2.urlopen(urlgetphoto).read()
        dataphoto = simplejson.loads(getphotopage)
        singlephotodata = dataphoto["sizes"]["size"][1]["source"]
        returndata = json.dumps({
        "singlephotodata": singlephotodata,
                                })
        return returndata