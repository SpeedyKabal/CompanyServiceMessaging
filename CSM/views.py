from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.http.response import HttpResponseRedirect
from .decorators import unauthenticated_user, authenticated_user
from .models import Employee
from .forms import EmployeeForm, UserForm

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


@authenticated_user
def signMeOut(request):
    auth.logout(request)
    return HttpResponseRedirect("/")


@authenticated_user
def home(request):
        employee = Employee.objects.get(user = request.user)
        return render(request, "CSM/home.html", {'employee' : employee})


def profile(request, profile_user):
    # Using get_object_or_404 to raise a 404 if the user doesn't exist
    userp = get_object_or_404(Employee, user__username = profile_user)
    return render(request, "CSM/profile.html", {
        'userprofile': userp})


def settings(request):
    user_profile = Employee.objects.get(user=request.user)
    user_profile1 = User.objects.get(username=request.user)

    employee = EmployeeForm(request.POST, instance=user_profile)
    worker = UserForm(request.POST, instance=user_profile1)

    if request.method == 'POST':
        employee = EmployeeForm(request.POST, instance=user_profile)
        worker = UserForm(request.POST, instance=user_profile1)
        if employee.is_valid() and worker.is_valid():
            employee.save()
            worker.save()
            return redirect("CSM:Profile", profile_user = worker.cleaned_data['username'])
        else:
            employee = EmployeeForm(instance = user_profile)
            worker = UserForm(request.POST, instance=user_profile1)
    return render(request, "CSM/Settings.html", { 'form' : employee,
                                                 'user': worker } )

def sendMessage(request):
    return render(request, "CSM/send_message.html")
