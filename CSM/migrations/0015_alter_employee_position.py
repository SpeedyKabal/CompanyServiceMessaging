# Generated by Django 4.2.7 on 2023-12-12 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSM', '0014_alter_employee_birthday_alter_employee_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(blank=True, choices=[('director', 'Director'), ('statistique', 'Ingénieur etat en statistique'), ('informatique', 'Ingénieur etat en informatique'), ('ts_informatique', 'Technicien supérieur en informatique'), ('Medecin_generaliste', 'Médecin généraliste de sante publique'), ('infirmier', 'Infirmier de sante publique'), ('comptable', 'Comptable administratif'), ('Adm_Principal', 'Administrateur principal'), ('Adm_Analyste', 'Administrateur analyste'), ('Agent_prev_1', 'Agent de prévention de niveau 1'), ('Agent_Adm', 'Agent d`administration'), ('Agent_Bureau', 'Agent de bureau'), ('Medecin_generaliste_chef', 'Médecin généraliste en chef de santé publique'), ('Assistant ing nv 2 en informatique', 'Assistant ingénieur de niveau 2 en informatique')], max_length=64, null=True),
        ),
    ]