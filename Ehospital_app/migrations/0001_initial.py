# Generated by Django 5.0.6 on 2024-06-02 19:28

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientId', models.PositiveIntegerField(null=True)),
                ('doctorId', models.PositiveIntegerField(null=True)),
                ('patientName', models.CharField(max_length=40, null=True)),
                ('doctorName', models.CharField(max_length=40, null=True)),
                ('message', models.TextField(max_length=500, null=True)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientId', models.PositiveIntegerField(null=True)),
                ('doctorId', models.PositiveIntegerField(null=True)),
                ('doctorUserName', models.CharField(max_length=40, null=True)),
                ('patientName', models.CharField(max_length=40, null=True)),
                ('doctorName', models.CharField(max_length=40, null=True)),
                ('bookedDate', models.DateTimeField(auto_now=True)),
                ('appointmentDate', models.DateField(default=django.utils.timezone.now)),
                ('appointmentTime', models.CharField(max_length=20, null=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospitalName', models.CharField(max_length=40, null=True)),
                ('hospitalId', models.PositiveIntegerField(null=True)),
                ('address', models.CharField(max_length=40, null=True)),
                ('email', models.EmailField(max_length=40)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('description', models.TextField(max_length=500)),
                ('hospital_pic', models.ImageField(blank=True, null=True, upload_to='hospital_pic/')),
            ],
        ),
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientId', models.PositiveIntegerField(null=True)),
                ('pharmacistId', models.PositiveIntegerField(null=True)),
                ('doctorId', models.PositiveIntegerField(null=True)),
                ('labTechId', models.PositiveIntegerField(null=True)),
                ('patientName', models.CharField(max_length=40, null=True)),
                ('labTechName', models.CharField(max_length=40, null=True)),
                ('pharmacistName', models.CharField(max_length=40, null=True)),
                ('doctorName', models.CharField(max_length=40, null=True)),
                ('sampleType', models.TextField(max_length=500, null=True)),
                ('orderDate', models.DateTimeField(null=True)),
                ('user_id', models.PositiveIntegerField(null=True)),
                ('amount', models.PositiveIntegerField(null=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='LabTechRequestPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientId', models.PositiveIntegerField(null=True)),
                ('pharmacistId', models.PositiveIntegerField(null=True)),
                ('doctorId', models.PositiveIntegerField(null=True)),
                ('labTechId', models.PositiveIntegerField(null=True)),
                ('patientName', models.CharField(max_length=40, null=True)),
                ('labTechName', models.CharField(max_length=40, null=True)),
                ('pharmacistName', models.CharField(max_length=40, null=True)),
                ('doctorName', models.CharField(max_length=40, null=True)),
                ('sampleType', models.TextField(max_length=500, null=True)),
                ('orderDate', models.DateField(null=True)),
                ('description', models.CharField(max_length=50, null=True)),
                ('testPrice', models.PositiveIntegerField(null=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientId', models.PositiveIntegerField(null=True)),
                ('doctorId', models.PositiveIntegerField(null=True)),
                ('patientName', models.CharField(max_length=40, null=True)),
                ('doctorName', models.CharField(max_length=40, null=True)),
                ('medicineName', models.CharField(max_length=40, null=True)),
                ('quantity', models.PositiveIntegerField(null=True)),
                ('price', models.PositiveIntegerField(null=True)),
                ('Date', models.DateField(null=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PatientLabResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientId', models.PositiveIntegerField(null=True)),
                ('doctorId', models.PositiveIntegerField(null=True)),
                ('labTechId', models.PositiveIntegerField(null=True)),
                ('patientName', models.CharField(max_length=40, null=True)),
                ('labTechName', models.CharField(max_length=40, null=True)),
                ('doctorName', models.CharField(max_length=40, null=True)),
                ('sampleType', models.TextField(max_length=500, null=True)),
                ('orderDate', models.DateField(null=True)),
                ('labResult', models.TextField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PatientMedicineInstruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientId', models.PositiveIntegerField(null=True)),
                ('pharmacistId', models.PositiveIntegerField(null=True)),
                ('doctorId', models.PositiveIntegerField(null=True)),
                ('patientName', models.CharField(max_length=40, null=True)),
                ('pharmacistName', models.CharField(max_length=40, null=True)),
                ('doctorName', models.CharField(max_length=40, null=True)),
                ('medicine', models.CharField(max_length=40, null=True)),
                ('dosage', models.CharField(max_length=40, null=True)),
                ('numberOfDays', models.PositiveIntegerField(null=True)),
                ('instruction', models.TextField(max_length=500, null=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PatientPayementDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientId', models.PositiveIntegerField(null=True)),
                ('fullName', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('phone', models.CharField(max_length=13)),
                ('amount', models.PositiveIntegerField()),
                ('receiver', models.CharField(max_length=40)),
                ('receiverAccount', models.CharField(max_length=40)),
                ('paymentDate', models.DateField(null=True)),
                ('paymentTime', models.DateTimeField(auto_now=True)),
                ('transactionId', models.CharField(max_length=40)),
                ('total', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PharmacistRequestPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientId', models.PositiveIntegerField(null=True)),
                ('pharmacistId', models.PositiveIntegerField(null=True)),
                ('doctorId', models.PositiveIntegerField(null=True)),
                ('patientName', models.CharField(max_length=40, null=True)),
                ('pharmacistName', models.CharField(max_length=40, null=True)),
                ('doctorName', models.CharField(max_length=40, null=True)),
                ('medicine', models.CharField(max_length=40, null=True)),
                ('dosage', models.CharField(max_length=40, null=True)),
                ('numberOfDays', models.PositiveIntegerField(null=True)),
                ('description', models.CharField(max_length=50, null=True)),
                ('medicinePrice', models.PositiveIntegerField(null=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientId', models.PositiveIntegerField(null=True)),
                ('pharmacistId', models.PositiveIntegerField(null=True)),
                ('doctorId', models.PositiveIntegerField(null=True)),
                ('patientName', models.CharField(max_length=40, null=True)),
                ('pharmacistName', models.CharField(max_length=40, null=True)),
                ('doctorName', models.CharField(max_length=40, null=True)),
                ('medicine', models.CharField(max_length=40, null=True)),
                ('dosage', models.CharField(max_length=40, null=True)),
                ('numberOfDays', models.CharField(max_length=40, null=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RoomMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('uid', models.CharField(max_length=1000)),
                ('room_name', models.CharField(max_length=200)),
                ('insession', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctorId', models.PositiveIntegerField(null=True)),
                ('doctorName', models.CharField(max_length=40, null=True)),
                ('doctorDepartment', models.CharField(max_length=40, null=True)),
                ('morning_1', models.CharField(max_length=10, null=True)),
                ('morning_2', models.CharField(max_length=10, null=True)),
                ('morning_3', models.CharField(max_length=10, null=True)),
                ('morning_4', models.CharField(max_length=10, null=True)),
                ('morning_5', models.CharField(max_length=10, null=True)),
                ('morning_6', models.CharField(max_length=10, null=True)),
                ('morning_7', models.CharField(max_length=10, null=True)),
                ('morning_8', models.CharField(max_length=10, null=True)),
                ('morning_9', models.CharField(max_length=10, null=True)),
                ('morning_10', models.CharField(max_length=10, null=True)),
                ('morning_11', models.CharField(max_length=10, null=True)),
                ('morning_12', models.CharField(max_length=10, null=True)),
                ('afternoon_1', models.CharField(max_length=10, null=True)),
                ('afternoon_2', models.CharField(max_length=10, null=True)),
                ('afternoon_3', models.CharField(max_length=10, null=True)),
                ('afternoon_4', models.CharField(max_length=10, null=True)),
                ('afternoon_5', models.CharField(max_length=10, null=True)),
                ('afternoon_6', models.CharField(max_length=10, null=True)),
                ('afternoon_7', models.CharField(max_length=10, null=True)),
                ('afternoon_8', models.CharField(max_length=10, null=True)),
                ('afternoon_9', models.CharField(max_length=10, null=True)),
                ('afternoon_10', models.CharField(max_length=10, null=True)),
                ('afternoon_11', models.CharField(max_length=10, null=True)),
                ('afternoon_12', models.CharField(max_length=10, null=True)),
                ('evening_1', models.CharField(max_length=10, null=True)),
                ('evening_2', models.CharField(max_length=10, null=True)),
                ('evening_3', models.CharField(max_length=10, null=True)),
                ('evening_4', models.CharField(max_length=10, null=True)),
                ('evening_5', models.CharField(max_length=10, null=True)),
                ('evening_6', models.CharField(max_length=10, null=True)),
                ('evening_7', models.CharField(max_length=10, null=True)),
                ('evening_8', models.CharField(max_length=10, null=True)),
                ('evening_9', models.CharField(max_length=10, null=True)),
                ('evening_10', models.CharField(max_length=10, null=True)),
                ('evening_11', models.CharField(max_length=10, null=True)),
                ('evening_12', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientId', models.PositiveIntegerField(null=True)),
                ('patientName', models.CharField(max_length=40, null=True)),
                ('symptomId', models.PositiveIntegerField(null=True)),
                ('symptoms', models.TextField(max_length=500, null=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Symptomm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TestPay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientId', models.PositiveIntegerField(null=True)),
                ('payername', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('phone', models.CharField(max_length=13)),
                ('amount', models.PositiveIntegerField()),
                ('receiver', models.CharField(max_length=40)),
                ('receiverAccount', models.CharField(max_length=40)),
                ('paymentDate', models.DateField(null=True)),
                ('paymentTime', models.DateTimeField(auto_now=True)),
                ('transactionId', models.CharField(max_length=40)),
                ('total', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/DoctorProfilePic/')),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(blank=True, max_length=15)),
                ('email', models.EmailField(max_length=40)),
                ('department', models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('EmergencyDepartement', 'EmergencyDepartement'), ('Psychiatrist', 'Psychiatrist'), ('Dermatologist', 'Dermatologist'), ('Allergist', 'Allergist'), ('Pediatrician', 'Pediatrician'), ('Orthopedist', 'Orthopedist'), ('Anesthesiologist', 'Anesthesiologist'), ('Oncologist', 'Oncologist'), ('Nephrologist', 'Nephrologist'), ('GeneralPhysician', 'GeneralPhysician')], default='Dermatologist', max_length=50)),
                ('expriance', models.PositiveIntegerField(null=True)),
                ('certification', models.ImageField(blank=True, null=True, upload_to='profile_pic/DoctorCertification/')),
                ('hospital_name', models.CharField(max_length=40)),
                ('admitDate', models.DateField(null=True)),
                ('todayDate', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
                ('is_avialable', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LabTech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/LabTechProfilePic/')),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=40)),
                ('hospital_name', models.CharField(max_length=40)),
                ('status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/PatientProfilePic/')),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=40, null=True)),
                ('admitDate', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/PharmacistProfilePic/')),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=40)),
                ('hospital_name', models.CharField(max_length=40)),
                ('status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorRecommondation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('recommended_doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patients', to='Ehospital_app.doctor')),
                ('symptoms', models.ManyToManyField(to='Ehospital_app.symptomm')),
            ],
        ),
    ]