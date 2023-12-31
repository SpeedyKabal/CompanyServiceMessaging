from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Employee, Messages



@receiver(post_save, sender=User)
def created_employee(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)


@receiver(post_save, sender=Messages)
def mark_message_as_unread(sender, instance, created, **kwargs):
    if created:
        instance.is_read = False
        instance.save()
'''
@receiver(post_save, sender=User)
def updated_employee(sender, instance, created, **kwargs):
    if not created:
        instance.employee.save()
'''