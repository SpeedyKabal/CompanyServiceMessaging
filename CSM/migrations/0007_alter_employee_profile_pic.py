# Generated by Django 4.2.7 on 2023-11-28 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSM', '0006_employee_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile_pic.png', null=True, upload_to=''),
        ),
    ]
