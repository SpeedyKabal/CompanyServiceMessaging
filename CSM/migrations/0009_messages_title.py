# Generated by Django 4.2.7 on 2023-12-03 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSM', '0008_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='title',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]