from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


departments = [ 
            ('Cardiologist','Cardiologist'),
            ('EmergencyDepartment','EmergencyDepartment'),
            ('Psychiatrist','Psychiatrist'),
            ('Dermatologist','Dermatologist'),
            ('Allergist','Allergist'),
            ('Pediatrician','Pediatrician'),
            ('Orthopedist','Orthopedist'),
            ('Anesthesiologist','Anesthesiologist'),
            ('Oncologist','Oncologist'),
            ('Nephrologist','Nephrologist'),
            ('GeneralPhysician','GeneralPhysician'),

            ]


class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=15, blank=True)
    email=models.EmailField(max_length=40)
    department= models.CharField(max_length=50,choices=departments,default='Dermatologist')
    expriance = models.PositiveIntegerField(null=True)
    certification= models.ImageField(upload_to='profile_pic/DoctorCertification/',null=True,blank=True)
    hospital_name=models.CharField(max_length=40)
    admitDate=models.DateField(null=True)
    todayDate=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)
    is_avialable=models.BooleanField(default=False)


    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name 
    @property
    def get_id(self):
        return self.user.id
    @property
    def doctor_username(self):
        return self.user.username

    def __str__(self):
         return "Dr."+" "+ self.user.first_name


class Symptom(models.Model):
    name = models.CharField(max_length=100)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.name


class DoctorRecommondation(models.Model):
    name = models.CharField(max_length=100)
    symptoms = models.ManyToManyField(Symptom)
    recommended_doctor = models.ManyToManyField(Doctor, blank=True)
    selected_symptoms = models.CharField(max_length=100,null=True)
    symptmId = models.CharField(max_length=100,null=True)
    patent_Id = models.CharField(max_length=100,null=True)


    def display_symptoms(self):
        return ", ".join([symptom.name for symptom in self.symptoms.all()])
    
    def get_sy(self):
        return self.symptoms

    def __str__(self):
        return self.name


class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40,)
    mobile = models.CharField(max_length=13,null=False)
    email=models.EmailField(max_length=40,null=True)
    admitDate=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)
    is_discharged=models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "Patient"+" "+self.user.first_name

class ScheduleAppointment(models.Model):
    doctorId = models.PositiveIntegerField(null=True)
    doctorName = models.CharField(max_length=40, null=True)
    doctorDepartment = models.CharField(max_length=40, null=True)

    morning_1 = models.CharField(max_length=10, null=True)
    morning_2 = models.CharField(max_length=10, null=True) 
    morning_3 = models.CharField(max_length=10, null=True) 
    morning_4 = models.CharField(max_length=10, null=True) 
    morning_5 = models.CharField(max_length=10, null=True) 
    morning_6 = models.CharField(max_length=10, null=True)  
    morning_7 = models.CharField(max_length=10, null=True) 
    morning_8 = models.CharField(max_length=10, null=True) 
    morning_9 = models.CharField(max_length=10, null=True) 
    morning_10 = models.CharField(max_length=10, null=True) 
    morning_11 = models.CharField(max_length=10, null=True) 
    morning_11 = models.CharField(max_length=10, null=True)  
    morning_11 = models.CharField(max_length=10, null=True)  
    morning_12 = models.CharField(max_length=10, null=True)  

    afternoon_1 = models.CharField(max_length=10, null=True) 
    afternoon_2 = models.CharField(max_length=10, null=True) 
    afternoon_3 = models.CharField(max_length=10, null=True) 
    afternoon_4 = models.CharField(max_length=10, null=True) 
    afternoon_5 = models.CharField(max_length=10, null=True) 
    afternoon_6 = models.CharField(max_length=10, null=True) 
    afternoon_7 = models.CharField(max_length=10, null=True) 
    afternoon_8 = models.CharField(max_length=10, null=True) 
    afternoon_9 = models.CharField(max_length=10, null=True) 
    afternoon_10 = models.CharField(max_length=10, null=True) 
    afternoon_11 = models.CharField(max_length=10, null=True) 
    afternoon_12 = models.CharField(max_length=10, null=True) 

    evening_1 = models.CharField(max_length=10, null=True) 
    evening_2 = models.CharField(max_length=10, null=True) 
    evening_3 = models.CharField(max_length=10, null=True) 
    evening_4 = models.CharField(max_length=10, null=True) 
    evening_5 = models.CharField(max_length=10, null=True) 
    evening_6 = models.CharField(max_length=10, null=True) 
    evening_7 = models.CharField(max_length=10, null=True) 
    evening_8 = models.CharField(max_length=10, null=True) 
    evening_9 = models.CharField(max_length=10, null=True) 
    evening_10 = models.CharField(max_length=10, null=True) 
    evening_11 = models.CharField(max_length=10, null=True) 
    evening_12 = models.CharField(max_length=10, null=True) 




class Appointment(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    doctorUserName=models.CharField(max_length=40,null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    bookedDate=models.DateTimeField(auto_now=True)
    appointmentDate=models.DateField(default=timezone.now)
    appointmentTime = models.CharField(max_length=20, null=True)
    status=models.BooleanField(default=False)



  
class Hospital(models.Model):
    hospitalName=models.CharField(max_length=40,null=True)
    hospitalId=models.PositiveIntegerField(null=True)
    address=models.CharField(max_length=40,null=True)
    email=models.EmailField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    description=models.TextField(max_length=500) 
    hospital_pic = models.ImageField(upload_to='hospital_pic/',null=True,blank=True)
    def __str__(self):
        return  self.hospitalName+ " " +"Hospital"



class Pharmacist(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/PharmacistProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=13,null=False)
    email=models.EmailField(max_length=40)
    hospital_name=models.CharField(max_length=40)
    status=models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "Pharmacist "+ self.user.first_name



class LabTech(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/LabTechProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=13,null=False)
    email=models.EmailField(max_length=40)
    hospital_name=models.CharField(max_length=40) 
    status=models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name



class Medicine(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    medicineName=models.CharField(max_length=40,null=True)
    quantity=models.PositiveIntegerField(null=True) 
    price=models.PositiveIntegerField(null=True)
    Date=models.DateField(null=True)
    status=models.BooleanField(default=False)



class Prescription(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    pharmacistId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    pharmacistName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    medicine=models.CharField(max_length=40,null=True)
    dosage=models.CharField(max_length=40,null=True)
    numberOfDays=models.CharField(max_length=40,null=True)
    status=models.BooleanField(default=False)

    @property
    def get_id(self):
        return self.user.id



class Laboratory(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    pharmacistId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    labTechId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    labTechName=models.CharField(max_length=40,null=True)
    pharmacistName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    sampleType=models.TextField(max_length=500,null=True)
    orderDate=models.DateTimeField(null=True) 
    user_id=models.PositiveIntegerField(null=True)
    amount=models.PositiveIntegerField(null=True)
    status=models.BooleanField(default=False)



class LabTechRequestPayment(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    pharmacistId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    labTechId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    labTechName=models.CharField(max_length=40,null=True)
    hospitalName=models.CharField(max_length=40,null=True)
    pharmacistName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    sampleType=models.TextField(max_length=500,null=True)
    orderDate=models.DateField(null=True) 
    description=models.CharField(max_length=50,null=True)
    testPrice=models.PositiveIntegerField(null=True)
    status=models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.patientName



class PharmacistRequestPayment(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    pharmacistId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    pharmacistName=models.CharField(max_length=40,null=True)
    hospitalName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    medicine=models.CharField(max_length=40,null=True)
    dosage=models.CharField(max_length=40,null=True)
    numberOfDays=models.PositiveIntegerField(null=True)
    description=models.CharField(max_length=50,null=True)
    medicinePrice=models.PositiveIntegerField(null=True)
    status=models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.patientName




class RoomMember(models.Model):
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=1000)
    room_name = models.CharField(max_length=200)
    insession = models.BooleanField(default=True)

    def __str__(self):
        return self.name




class PatientPayementDetail(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    fullName=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    phone=models.CharField(max_length=13)
    amount=models.PositiveIntegerField(null=False)
    receiver=models.CharField(max_length=40)
    receiverAccount=models.CharField(max_length=40)
    paymentDate=models.DateField(null=True)  
    paymentTime=models.DateTimeField(auto_now=True)  
    transactionId=models.CharField(max_length=40)
    total=models.PositiveIntegerField(null=False)



class PatientLabResult(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    labTechId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    labTechName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    sampleType=models.TextField(max_length=500,null=True)
    orderDate=models.DateField(null=True) 
    labResult=models.TextField(max_length=500,null=True)
  


class PatientMedicineInstruction(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    pharmacistId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    pharmacistName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    medicine=models.CharField(max_length=40,null=True)
    dosage=models.CharField(max_length=40,null=True) 
    numberOfDays=models.PositiveIntegerField(null=True)
    instruction=models.TextField(max_length=500,null=True)
    status=models.BooleanField(default=False)



class TestPay(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    payername=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    phone=models.CharField(max_length=13)
    amount=models.PositiveIntegerField(null=False)
    receiver=models.CharField(max_length=40)
    receiverAccount=models.CharField(max_length=40)
    paymentDate=models.DateField(null=True)  
    paymentTime=models.DateTimeField(auto_now=True)  
    transactionId=models.CharField(max_length=40)
    total=models.PositiveIntegerField(null=True)


class Announcement(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    message=models.TextField(max_length=500,null=True)
    date=models.DateField(auto_now=True)

  
