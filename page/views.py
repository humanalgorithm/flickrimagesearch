


from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def fourzerofour(request):
    return render(request, "fourzerofour.html")
