from django.urls import path
from . import views

app_name = "CSM"

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.signMeUp, name="SignUp"),
    path("home", views.home, name="home"),
    path("Logout", views.signMeOut, name="SignOut")
]