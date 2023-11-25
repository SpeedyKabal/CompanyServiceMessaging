from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, authenticated_user
from .models import Employee

# Create your views here.

@unauthenticated_user
def index(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("CSM:home")
        else:
            messages.error(request,"Username or Password Incorrect")
            return redirect("CSM:index")

    return render(request, "CSM/index.html")


@unauthenticated_user
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
                return redirect("CSM:SignUp")
            elif User.objects.filter(username=username).exists():
                messages.error(request, "Username Not Available")
                return redirect("CSM:SignUp")
            else:
                user=User.objects.create_user(username=username, first_name=first_name, last_name=last_name,email=email, password=password1)
                user.save()
                return HttpResponseRedirect("/")
        else:
            messages.error(request, "Password Not Matched !!")
            return redirect("CSM:SignUp")
    return render(request, "CSM/signUP.html")



def signMeOut(request):
    auth.logout(request)
    return HttpResponseRedirect("/")



@authenticated_user
def home(request):
        return render(request, "CSM/home.html")


def profile(request, user_profile):
    # Using get_object_or_404 to raise a 404 if the user doesn't exist
    userp = get_object_or_404(Employee, user__username = user_profile)
    return render(request, "CSM/profile.html", {
        'userprofile': userp})