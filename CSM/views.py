from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def index(request):
    #try:
        return render(request, "Pages/index.html", {'name' : "Variable Value"})
    #except:
        #return HttpResponseNotFound("<h1>Page Not Found</h1>")


def signMeUp(request):
        return render(request, "Pages/signUP.html")