# Generated by Django 5.0.6 on 2024-06-05 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ehospital_app', '0009_labtechrequestpayment_hospitalname'),
    ]

    operations = [
        migrations.AddField(
            model_name='pharmacistrequestpayment',
            name='hospitalName',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
