from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm
from django.contrib import auth
from django.contrib.auth import update_session_auth_hash
from django.http.response import HttpResponseRedirect
from .decorators import unauthenticated_user, authenticated_user
from .models import Employee, Messages, Files
from .forms import EmployeeForm, UserForm
from django.utils import timezone
import re, os, uuid
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.serializers import serialize
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@unauthenticated_user
def index(request):
    if request.method == "POST":
        username = request.POST['username'].lower()
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
        username = request.POST['username'].lower()
        first_name = request.POST['first_name'].capitalize()
        last_name = request.POST['last_name'].upper()
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
    try:
        allMessages = Messages.objects.filter(reciever = request.user).select_related('sender__employee')    
        unread_messages = Messages.objects.filter(reciever = request.user, is_read = False).values_list('id',flat=True)
    except Messages.DoesNotExist:
        allMessages = 0
        unread_messages = 0

    context = {
        'messages' : allMessages,
        'unreaded' : unread_messages
    }


    return render(request, "CSM/home.html", context)


@authenticated_user
def profile(request, profile_user):
    # Using get_object_or_404 to raise a 404 if the user doesn't exist
    userp = get_object_or_404(Employee, user__username = profile_user)
    return render(request, "CSM/profile.html", {
        'userprofile': userp })


@authenticated_user
def PasswordsChangeView(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Password changed successfully.')
                return redirect("CSM:SignOut")
        else:
            form = SetPasswordForm(user=request.user)
    return(request, "CSM/updatePassword.html", {'form':form})


@authenticated_user
def settings(request):
    employee = Employee.objects.get(user  = request.user)
    userObject = User.objects.get(username=request.user)

    employeeForm = EmployeeForm(request.POST, instance=employee)
    userObjectForm = UserForm(request.POST, instance=userObject)
    if request.method == 'POST':
        employeeForm = EmployeeForm(request.POST,request.FILES, instance=employee)
        userObjectForm = UserForm(request.POST, instance=userObject)
        if employeeForm.is_valid() and userObjectForm.is_valid():
            employeeForm.save()
            userObjectForm.save()
            return redirect("CSM:Profile", profile_user = userObjectForm.cleaned_data['username'])
        else:
            employeeForm = EmployeeForm(instance = employee)
            userObjectForm = UserForm(request.POST, instance=userObject)
    return render(request, "CSM/Settings.html", {'employeeForm':employeeForm,
                                                 'userObjectForm':userObjectForm})


@authenticated_user
def sendMessage(request):
    employee = Employee.objects.get(user = request.user)
    recievers = User.objects.exclude(username=request.user).values('username','first_name','last_name')
    if request.method == "POST":
        sender = request.user
        reciever_username = request.POST['user_option']
        reciever = get_object_or_404(User, username=reciever_username)
        message = request.POST['user_message']
        messageTitle = request.POST['message_title']
        uploaded_files = request.FILES.getlist('files')
        sent_message = Messages.objects.create(sender=sender, reciever=reciever, message=message, title=messageTitle)
        sent_message.save()
        for fichier in uploaded_files:
            Files.objects.create(message_id=sent_message, file=fichier)

        return redirect("CSM:home")
    context = {
        'users':recievers ,
        'employee':employee
    }
    return render(request, "CSM/send_message.html", context)


@csrf_exempt 
def markItRead(request):
    if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        message_id = request.POST.get('message_id')
        try:
            message = Messages.objects.get(id=message_id)
        except Messages.DoesNotExist:
            message = 0
        files = Files.objects.filter(message_id = message_id)
        file_urls = [file.file.url for file in files]
        if not (message.is_read):
            message.is_read = True
            message.save()
        
        context = {
            'content': message.message,
            'title': message.title,
            'date': message.date_created, 
            'fichiers' : file_urls,
        }
        return JsonResponse(context)
    else:
        return JsonResponse({'error':'Invalid request'})
    

@csrf_exempt 
def getMyMessages(request):
    if request.method == 'POST':
        message_id = request.POST.get('message_id')
        try:
            message = Messages.objects.get(id=message_id)
        except Messages.DoesNotExist:
            message = {'message' : 'Not Found',
                       'title':'Not found',
                       'date_created':'Not Found'}
        files = Files.objects.filter(message_id = message_id)
        file_urls = [file.file.url for file in files]
        
        context = {
            'content': message.message,
            'title': message.title,
            'date': message.date_created, 
            'fichiers' : file_urls,
        }
        return JsonResponse(context)
    else:
        return JsonResponse({'error':'Invalid request'})


def fetch_new_messages(request):
    employeeId = request.GET.get('employeeId') #The Id of The Sender
    dateTime = request.GET.get('date_message') #The datetime to look on database of new messages that has date_created greater than this
    if employeeId is not None and dateTime is not None:
        lastCheck = timezone.datetime.fromisoformat(dateTime)
        new_messages = Messages.objects.filter(reciever_id = employeeId, date_created__gt = lastCheck, is_read = False)
        newMessageHtml = render_to_string('CSM/newUserHtml.html', {'messages': new_messages})
        return JsonResponse({'latestMessage' : newMessageHtml })
    else:
        return JsonResponse({'error' : 'User Id or Last Ckeck time not Provided'})
    

def fetch_new_messages_for_notification(request):
    employeeId = request.GET.get('employeeId') #The Id of The Sender
    if employeeId is not None:
        new_messages = Messages.objects.filter(reciever_id = employeeId, is_read = False).count()
        return JsonResponse({'notifications' : new_messages })
    else:
        return JsonResponse({'error' : 'User Id or Last Ckeck time not Provided'})
    

@authenticated_user
def inbox(request):
    try:
        allMessages = Messages.objects.filter(sender = request.user)
        unread_messages = Messages.objects.filter(sender = request.user, is_read = False).values_list('id',flat=True)
    except Messages.DoesNotExist:
        allMessages = 0
        unread_messages = 0

    context = {
        'messages' : allMessages,
        'unreaded' : unread_messages
    }
    return render(request, "CSM/inbox.html", context)


@authenticated_user
def allUserProfiles(request):
    allUser = User.objects.all()
    return render(request, "CSM/allUsersPage.html", {'users' : allUser})
