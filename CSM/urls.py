from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name = "CSM"

urlpatterns = [
    path('', views.index, name="loginPage"),
    path('register/', views.signMeUp, name="SignUp"),
    path('home/', views.home, name="home"),
    path('inbox/', views.inbox, name="inbox"),
    path('markItRead/', views.markItRead, name='markItRead'),
    path('submitResponse/', views.submitResponse, name='submitResponse'),
    path('getnewmessages/', views.fetch_new_messages, name='newMessages'),
    path('getMyMessages/', views.getMyMessages, name='MyMessages'),
    path('getnewmessagesNotifications/', views.fetch_new_messages_for_notification, name='newMessagesNotification'),
    path('Logout/', views.signMeOut, name="SignOut"),
    path('settings/', views.settings, name="Setting"),
    path('changepassword/', views.PasswordsChangeView, name="changePassword"),
    path('send_message/', views.sendMessage, name="Send_Message"),
    path('allemployees/', views.allUserProfiles, name="AllProfiles"),
    path('<str:profile_user>/', views.profile , name="Profile")
]