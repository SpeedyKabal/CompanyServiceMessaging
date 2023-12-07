# Generated by Django 4.2.7 on 2023-12-06 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSM', '0009_messages_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='ar_position',
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(choices=[('director', 'Director'), ('statistique', 'Statistical Engineering'), ('informatique', 'Informatic Engineering'), ('informatique_ts', 'Informatic Technical Senior')], max_length=64, null=True),
        ),
    ]