# admin.py
from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_filter = ['position', 'gender','user__date_joined', 'user__last_login']
    list_display = ['get_username','get_first_name','get_last_name','gender','position']

    def get_username(self, obj):
        return obj.user.username
    

    def get_first_name(self, obj):
        return obj.user.first_name
    

    def get_last_name(self, obj):
        return obj.user.last_name
    
    
    get_username.short_description = "Username"
    get_first_name.short_description = "First Name"
    get_last_name.short_description = "Last Name"



admin.site.register(Employee, EmployeeAdmin)
