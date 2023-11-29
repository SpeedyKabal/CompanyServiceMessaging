from django.urls import path
from . import views

app_name = "CSM"

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.signMeUp, name="SignUp"),
    path("home/", views.home, name="home"),
    path("Logout/", views.signMeOut, name="SignOut"),
    path("settings/", views.settings, name="Setting"),
    path("send_message/", views.sendMessage, name="Send_Message"),
    path("<str:profile_user>/", views.profile, name="Profile"),
]