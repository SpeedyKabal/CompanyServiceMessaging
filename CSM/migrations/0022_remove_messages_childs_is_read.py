# Generated by Django 4.2.7 on 2023-12-18 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CSM', '0021_alter_messages_childs_is_read'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='childs_is_read',
        ),
    ]
