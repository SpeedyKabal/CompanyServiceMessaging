# Generated by Django 4.2.3 on 2023-12-19 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CSM', '0018_messages_child_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='child_message',
        ),
    ]