# Generated by Django 5.0.6 on 2024-06-09 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ehospital_app', '0011_patient_is_discharged'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='is_discharged',
        ),
    ]