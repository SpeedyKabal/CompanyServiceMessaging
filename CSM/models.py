# CSM/models.py
from django.db import models
from django.contrib.auth.models import User

# Users Table
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    master = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)


#Table which save the sender and the reciever of Messages 
class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


#Table which save the sender and the reciever of files 
class File(models.Model):
    sender = models.ForeignKey(User, related_name='uploaded_files', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    timestamp = models.DateTimeField(auto_now_add=True)
