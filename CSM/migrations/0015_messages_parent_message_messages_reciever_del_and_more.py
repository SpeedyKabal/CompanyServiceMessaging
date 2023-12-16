# Generated by Django 4.2.3 on 2023-12-12 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CSM', '0014_alter_employee_birthday_alter_employee_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='parent_message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='CSM.messages'),
        ),
        migrations.AddField(
            model_name='messages',
            name='reciever_del',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='messages',
            name='sender_del',
            field=models.BooleanField(default=False),
        ),
    ]