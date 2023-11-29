from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    GENDER = (
        ('Male','Male'),
        ('Female','Female')
    )
    POSITION = (
        ('Director','Director'),
        ('Statistical Engineering','Statistical Engineering'),
        ('Informatic Engineering','Informatic Engineering'),
        ('Informatic Technical Senior','Informatic Technical Senior')
    )
    ARPOSITION = (
        ('مدير المؤسسة','مدير المؤسسة'),
        ('مهندس دولة في الإحصاء','مهندس دولة في الإحصاء'),
        ('مهندس دولة في الإعلام الألي','مهندس دولة في الإعلام الألي'),
        ('تقني سامي في الإعلام الألي','تقني سامي في الإعلام الألي')
    )
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    gender = models.CharField(max_length=6, null=True, choices=GENDER)
    phone = models.CharField(max_length=10, null=True, blank=True)
    adress = models.TextField(max_length=60, null=True, blank=True)
    position = models.CharField(max_length=40, null=True, choices=POSITION)
    ar_position = models.CharField(max_length=40, null=True, choices=ARPOSITION)
    birthday = models.DateField(null=True)
    profile_pic = models.ImageField(null=True,blank=True, default='profile_pic.png')


    def __str__(self):
        return self.user.username 



