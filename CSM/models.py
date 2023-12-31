from django.db import models
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.utils import timezone
import os
from datetime import datetime

POSITION = {
    'None' : {'en':'Not Specified Yet','ar':'لم يتم التحديد بعد'},
    'director' : {'en':'Director','ar':'مدير المؤسسة'},
    'statistique' : {'en':'Ingénieur etat en statistique','ar':'مهندس دولة في الإحصائيات'},
    'informatique' : {'en':'Ingénieur etat en informatique','ar':'مهندس دولة في الإعلام الآلي'},
    'ts_informatique' : {'en':'Technicien supérieur en informatique','ar':'تقني سامي في الإعلام الآلي'},
    'Medecin_generaliste' : {'en':'Médecin généraliste de sante publique','ar':'طبيب عام في الصحة العمومية'},
    'infirmier' : {'en':'Infirmier de sante publique','ar':'ممرض للصحة العمومية'},
    'comptable' : {'en':'Comptable administratif','ar':'محاسب إداري'},
    'Adm_Principal' : {'en':'Administrateur principal','ar':'متصرف رئيسي'},
    'Adm_Analyste' : {'en':'Administrateur analyste','ar':'متصرف محلل'},
    'Agent_prev_1' : {'en':'Agent de prévention de niveau 1','ar':'عون الوقاية من المستوى 1'},
    'Agent_Adm' : {'en':'Agent d`administration','ar':'عون إدارة'},
    'Agent_Bureau' : {'en':'Agent de bureau','ar':'عون مكتب'},
    'Medecin_generaliste_chef' : {'en':'Médecin généraliste en chef de santé publique','ar':'طبيب عام رئيس في الصحة العمومية'},
    'Assistant ing nv 2 en informatique' : {'en':'Assistant ingénieur de niveau 2 en informatique','ar':'رتبة مساعد مهندس مستوى 2 في الإعلام الآلي'},
}

class Employee(models.Model):
    GENDER = (
        ('Male','Male'),
        ('Female','Female')
    )

    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    gender = models.CharField(max_length=6, null=True, choices=GENDER)
    phone = models.CharField(max_length=10, null=True, blank=True)
    adress = models.CharField(max_length=128, null=True, blank=True)
    position = models.CharField(max_length=64, null=True, choices=[(key, value['en']) for key, value in POSITION.items()], blank=True, default='')
    birthday = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(null=True,blank=True, default='profile_pic.png')

    def get_arabic_position(self):
        selected_position = self.position
        return POSITION[selected_position]['ar']
    

    def get_english_position(self):
        selected_position = self.position
        return POSITION[selected_position]['en']

    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        return self.full_name() 
    
    def save(self, *args, **kwargs):
        # Ensure the username is always saved in lowercase
        self.user.username = self.user.username.lower()
        super(Employee, self).save(*args, **kwargs)


class Messages(models.Model):
    sender = models.ForeignKey(User, null=True,related_name='sent_messages', on_delete=models.SET_NULL)
    title = models.CharField(max_length=64, null=True, blank=True)
    message = models.TextField(max_length=256, null=False, blank=False)
    reciever = models.ForeignKey(User, null=True, related_name='recieve_messages', on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    sender_del = models.BooleanField(default=False)
    reciever_del = models.BooleanField(default=False)
    parent_message = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='responses')


    def __str__(self):
        return self.sender.last_name + " -> " + self.reciever.last_name + " : " + self.message[:5]
    
    #Get The First Message to Make it Parent To all other Responses  
    def getParentMessage(self):
        if self.parent_message:
            return self.parent_message.getParentMessage()
        else:
            return self

    def message_and_responses_to_dict(self):
        #Recursively convert Messages instance and its responses to a dictionary.
        message_dict = model_to_dict(self)
        message_dict['date'] = self.date_created.isoformat() if self.date_created else None
        message_dict['responses'] = [response.message_and_responses_to_dict() for response in self.responses.all()]

        return message_dict




def generate_filename(instance, filename):
    # Get the current date and time
    current_datetime = datetime.now()

    # Get the file extension
    _, file_extension = os.path.splitext(filename)

    # Generate a unique filename based on the current date and time
    unique_filename = f"{current_datetime.strftime('%Y%m%d%H%M%S')}{file_extension}"

    # Return the generated filename
    return unique_filename



class Files(models.Model):
    message_id = models.ForeignKey(Messages, related_name='fichiers',on_delete=models.CASCADE)
    file = models.FileField(upload_to=generate_filename)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.message_id.sender.last_name + " " + self.message_id.title[:10]

