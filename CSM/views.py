from django.shortcuts import render
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.http.response import HttpResponseRedirect
# Create your views here.


nam

def index(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("/home")
        else:
            messages.error(request,"Username or Password Incorrect")
            return HttpResponseRedirect("/")

    return render(request, "Pages/index.html", {'name' : "Variable Value"})



def signMeUp(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email Already Existe")
                return HttpResponseRedirect("/register")
            elif User.objects.filter(username=username).exists():
                messages.error(request, "Username Not Available")
                return HttpResponseRedirect("/register")
            else:
                user=User.objects.create_user(username=username, first_name=first_name, last_name=last_name,email=email, password=password1)
                user.save()
                return HttpResponseRedirect("/")
        else:
            messages.error(request, "Password Not Matched !!")
            return HttpResponseRedirect("/register")
    return render(request, "Pages/signUP.html")

def signMeOut(request):
    auth.logout(request)
    return HttpResponseRedirect("/")



def home(request):
    return render(request, "Pages/home.html")