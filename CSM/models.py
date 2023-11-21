from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator, MaxFileSizeValidator

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    post = models.TextField(max_length=60, null=True)
    level = models.TextField(max_length=60, null=True) 
    master = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    title = models.TextField(max_length=150)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class File(models.Model):
    sender = models.ForeignKey(User, related_name='uploaded_files', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_files', on_delete=models.CASCADE)
    file = models.FileField(
        upload_to='uploads/%Y/%m/%d/',
                validators=[
            FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'txt', 'jpg', 'jpeg' , 'png'
            ]),  # Adjust allowed file extensions
            MaxFileSizeValidator(limit_bytes=100 * 1024 * 1024),  # 100 MB limit
        ])
    timestamp = models.DateTimeField(auto_now_add=True)