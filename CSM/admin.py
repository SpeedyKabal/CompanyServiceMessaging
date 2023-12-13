# admin.py
from django.contrib import admin
from .models import Employee, Messages, Files


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
    list_filter = ['sender__last_name', 'reciever__last_name',
                     'date_created', 'sender_del', 'reciever_del', 'responses']
    list_display = ['get_sender','get_message','get_reciever', 'date_created' ,'is_read']

    def get_sender(self, obj):
        return f"{obj.sender.first_name} {obj.sender.last_name}"
    

    def get_reciever(self, obj):
        return f"{obj.reciever.first_name} {obj.reciever.last_name}"
    
    def get_message(self, obj):
        words = obj.message.split()
        result = ' '.join(words[:3])
        return result

    get_sender.short_description = "Sender"
    get_reciever.short_description = "Reciecver"
    get_message.short_description = "Message"


class FilesAdmin(admin.ModelAdmin):
    list_filter = ['message_id__sender__last_name', 'message_id__reciever__last_name', 'date_created']
    list_display = ['get_file_sender','get_file_reciever','date_created', 'file']


    def get_file_sender(self, obj):
        return f"{obj.message_id.sender.first_name} {obj.message_id.sender.last_name}"
    

    def get_file_reciever(self, obj):
        return f"{obj.message_id.reciever.first_name} {obj.message_id.reciever.last_name}"
    

    get_file_sender.short_description = "Sender"
    get_file_reciever.short_description = "Reciecver"



admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Messages, MessagesAdmin)
admin.site.register(Files, FilesAdmin)
