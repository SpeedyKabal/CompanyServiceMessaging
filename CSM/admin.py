# admin.py
from django.contrib import admin
from .models import Employee, Messages


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


class MessagesAdmin(admin.ModelAdmin):
    list_filter = ['sender__last_name', 'reciever__last_name', 'date_created']
    list_display = ['get_sender','get_message','get_reciever', 'date_created' ,'is_read']

    def get_sender(self, obj):
        return obj.sender.last_name
    

    def get_reciever(self, obj):
        return obj.reciever.last_name
    
    def get_message(self, obj):
        words = obj.message.split()
        result = ' '.join(words[:3])
        return result

    get_sender.short_description = "Sender"
    get_reciever.short_description = "Reciecver"
    get_message.short_description = "Message"



admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Messages, MessagesAdmin)
