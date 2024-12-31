# Generated by Django 5.0.6 on 2024-06-03 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ehospital_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorrecommondation',
            name='selected',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('EmergencyDepartment', 'EmergencyDepartment'), ('Psychiatrist', 'Psychiatrist'), ('Dermatologist', 'Dermatologist'), ('Allergist', 'Allergist'), ('Pediatrician', 'Pediatrician'), ('Orthopedist', 'Orthopedist'), ('Anesthesiologist', 'Anesthesiologist'), ('Oncologist', 'Oncologist'), ('Nephrologist', 'Nephrologist'), ('GeneralPhysician', 'GeneralPhysician')], default='Dermatologist', max_length=50),
        ),
    ]