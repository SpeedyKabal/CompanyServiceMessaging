# Generated by Django 4.2.7 on 2023-12-18 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CSM', '0019_messages_childs_not_read'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messages',
            old_name='childs_not_read',
            new_name='childs_is_read',
        ),
    ]