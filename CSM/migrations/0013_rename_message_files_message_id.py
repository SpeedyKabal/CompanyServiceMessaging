# Generated by Django 4.2.3 on 2023-12-08 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CSM', '0012_files'),
    ]

    operations = [
        migrations.RenameField(
            model_name='files',
            old_name='message',
            new_name='message_id',
        ),
    ]