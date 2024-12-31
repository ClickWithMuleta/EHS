from django.shortcuts import render,redirect,reverse,HttpResponseRedirect
from . import forms,models
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,timedelta,date
from django.conf import settings
from django.contrib.auth.models import User,auth
from django.contrib import auth
from django.contrib.auth import login, authenticate,logout,get_user_model
from django.contrib import messages
from django.http import JsonResponse
import random
import time
from agora_token_builder import RtcTokenBuilder
from .models import RoomMember
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.core.exceptions import ValidationError
import random
import string
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
import requests



def index(request):
    doctors=models.Doctor.objects.all().filter(status=True)
    hospitals=models.Hospital.objects.all()
    return render(request,'hospital/index.html',{'doctors':doctors,'hospitals':hospitals})

def departement_view(request):
    return render(request,'hospital/departement.html')
    
def aboutus_view(request):
    return render(request,'hospital/about.html')

def services_view(request):
    return render(request,'hospital/services.html')

def hospital_detail_view(request,pk):
    hospitals=models.Hospital.objects.get(id=pk)
    hospitaldetails=models.Hospital.objects.all().filter(id=pk)
    return render(request,'hospital/hospital_detail.html',{'hospitals':hospitals,'hospitaldetails':hospitaldetails})

def doctor_detail_view(request,pk):
    doctors=models.Doctor.objects.get(id=pk)
    doctor=models.Doctor.objects.all().filter(id=pk)
    return render(request,'hospital/doctor_detail.html',{'doctors':doctors,'doctor':doctor})


def Cardiologist_departement_view(request):
    cardiologists=models.Doctor.objects.all().filter(status=True, department='Cardiologist')
    return render(request,'hospital/cardiologist_departement.html',{'cardiologists':cardiologists})

def Anesthesiologists_departement_view(request):
    anesthesiologists=models.Doctor.objects.all().filter(status=True, department='Anesthesiologist')
    return render(request,'hospital/anesthesiologist_departement.html',{'anesthesiologists':anesthesiologists})

def Dermatologists_departement_view(request):
    dermatologists=models.Doctor.objects.all().filter(status=True, department='Dermatologist')
    return render(request,'hospital/dermatologist_departement.html',{'dermatologists':dermatologists})

def Emergency_departement_view(request):
    emergencyDepartements=models.Doctor.objects.all().filter(status=True, department='EmergencyDepartement')
    return render(request,'hospital/emergency_departement.html',{'emergencyDepartements':emergencyDepartements})

def Allergists_departement_view(request):
    allergists=models.Doctor.objects.all().filter(status=True, department='Allergist')
    return render(request,'hospital/allergist_departement.html',{'allergists':allergists})

def Psychiatrist_departement_view(request):
    psychiatrists=models.Doctor.objects.all().filter(status=True, department='Colon and Rectal Surgeons')
    return render(request,'hospital/psychiatrist_departement.html',{'psychiatrists':psychiatrists})

def Pediatrician_departement_view(request):
    pediatricians=models.Doctor.objects.all().filter(status=True, department='Pediatrician')
    return render(request,'hospital/pediatrician_departement.html',{'pediatricians':pediatricians})

def Orthopedist_departement_view(request):
    orthopedists=models.Doctor.objects.all().filter(status=True, department='Orthopedist')
    return render(request,'hospital/orthopedist_departement.html',{'orthopedists':orthopedists})

def Oncologist_departement_view(request):
    oncologists=models.Doctor.objects.all().filter(status=True, department='Oncologist')
    return render(request,'hospital/oncologist_departement.html',{'oncologists':oncologists})

def Nephrologist_departement_view(request):
    nephrologists=models.Doctor.objects.all().filter(status=True, department='Nephrologist')
    return render(request,'hospital/nephrologist_departement.html',{'nephrologists':nephrologists})


#-----------for checking user is doctor , patient,pharmasict,lab_tech or admin
def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()
def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()
def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()
def is_pharmacist(user):
    return user.groups.filter(name='PHARMACIST').exists()
def is_lab_tech(user):
    return user.groups.filter(name='LAB_TECH').exists()


# def login_view(request):
#     message = None
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         recaptcha_response = request.POST.get('g-recaptcha-response')

#         # Verify reCAPTCHA
#         data = {
#             'secret': settings.RECAPTCHA_SECRET_KEY,
#             'response': recaptcha_response
#         }
#         r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
#         result = r.json()

#         if result['success']:
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 if is_admin(request.user):
#                     return redirect('admin-dashboard')
#                 elif is_doctor(request.user):
#                     return redirect('doctor-dashboard')
#                 elif is_patient(request.user):
#                     accountapproval = models.Patient.objects.all().filter(user_id=request.user.id, status=True)
#                     if accountapproval:
#                         return redirect('patient-dashboard')
#                     else:
#                         return render(request, 'hospital/patient_wait_for_approval.html')
#                 elif is_pharmacist(request.user):
#                     return redirect('pharmacist-dashboard')
#                 elif is_lab_tech(request.user):
#                     return redirect('labTech-dashboard')
#             else:
#                 messages.info(request, "Invalid Credentials")
#                 return render(request, 'hospital/login.html', {'message': message, 'site_key': settings.RECAPTCHA_SITE_KEY})
#         else:
#             messages.info(request, "You Must Pass reCAPTCHA Test.")
#             return render(request, 'hospital/login.html', {'message': message, 'site_key': settings.RECAPTCHA_SITE_KEY})
#     return render(request, 'hospital/login.html', {'message': message, 'site_key': settings.RECAPTCHA_SITE_KEY})



def login_view(request):
    message=None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if is_admin(request.user):
                return redirect('admin-dashboard') 
            elif is_doctor(request.user):
                return redirect('doctor-dashboard')

            elif is_patient(request.user):
                accountapproval=models.Patient.objects.all().filter(user_id=request.user.id,status=True)
                if accountapproval:
                    return redirect('patient-dashboard')
                else:
                    return render(request,'hospital/patient_wait_for_approval.html')
            elif is_pharmacist(request.user):
                return redirect('pharmacist-dashboard')

            elif is_lab_tech(request.user):
                return redirect('labTech-dashboard')  
        else:
            # Invalid credentials, display error message
            messages.info(request, "Invalid Credentials")
            return render(request, 'hospital/login.html',{'message':message})
    return render(request, 'hospital/login.html',{'message':message})
      
def logoutView(request):
	logout(request)
	return redirect('/')         

def admin_register_new_admin_view(request):
    if request.method=='POST':
        form=forms.RegisterAdminForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)
            return HttpResponseRedirect('login')
    else:
        form=forms.RegisterAdminForm()

    return render(request,'hospital/admin_register_new_admin.html.html',{'form':form})


# def patient_signup_view(request):
#     if request.method == 'POST':
#         userForm = forms.PatientUserForm(request.POST)
#         patientForm = forms.PatientForm(request.POST, request.FILES)
#         if userForm.is_valid() and patientForm.is_valid():
#             user = userForm.save(commit=False)
#             user.set_password(user.password)
#             user.save()

#             patient = patientForm.save(commit=False)
#             patient.user = user
#             patient.save()

#             my_patient_group, created = Group.objects.get_or_create(name='PATIENT')
#             my_patient_group.user_set.add(user)
            
#             return HttpResponseRedirect('/login')
#     else:
#         userForm = forms.PatientUserForm()
#         patientForm = forms.PatientForm()

#     mydict = {'userForm': userForm, 'patientForm': patientForm}
#     return render(request, 'hospital/patientsignup.html', context=mydict)



def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except:
        user = None

    if user is not None  and account_activation_token.check_token(user,token):
        user.is_active = True
        user.save()

        message = (
                f" Email Confirmation Success."
                 )
        messages.success(request, mark_safe(message))

        return redirect('/login')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('/')

 

def activateEmail(request, user, to_email):

    mail_subject = "Activate your user account."
    msg = render_to_string("hospital/template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })

    email = EmailMessage(mail_subject, msg, to=[to_email])
    if email.send():
        message = (
                    f'Dear <b>{user}</b>, please go to your email <b>{to_email}</b> inbox and click on \
                    received activation link to confirm and complete the registration. <b>Note:</b> If not exist in inbox check your spam folder.'
                )
        messages.success(request, mark_safe(message))

    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')


def patient_signup_view(request):
    if request.method == 'POST':
        userForm = forms.PatientUserForm(request.POST)
        patientForm = forms.PatientForm(request.POST, request.FILES)
        if userForm.is_valid() and patientForm.is_valid():
            user = userForm.save(commit=False)
            user.is_active=False
            user.set_password(user.password)
            user.save()

            patient = patientForm.save(commit=False)
            patient.user = user
            patient.status = True
            patient.save()

            my_patient_group, created = Group.objects.get_or_create(name='PATIENT')
            my_patient_group.user_set.add(user)

            activateEmail(request, user, patientForm.cleaned_data.get('email'))
            return HttpResponseRedirect('/')
    else:
        userForm = forms.PatientUserForm()
        patientForm = forms.PatientForm()

    mydict = {'userForm': userForm, 'patientForm': patientForm}
    return render(request, 'hospital/patientsignup.html', context=mydict)



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_dashboard_view(request):
    #for both table in admin dashboard
    doctors=models.Doctor.objects.all().order_by('-id')
    patients=models.Patient.objects.all().order_by('-id')
    #for three cards
    doctorcount=models.Doctor.objects.all().filter(status=True).count()
    patientcount=models.Patient.objects.all().filter(status=True).count()
    pendingpatientcount=models.Patient.objects.all().filter(status=False).count()
    hospitalcount=models.Hospital.objects.all().count()

    mydict={
    'doctors':doctors,
    'patients':patients,
    'doctorcount':doctorcount,
    'patientcount':patientcount,
    'pendingpatientcount':pendingpatientcount,

   'hospitalcount' :hospitalcount,
    }
    return render(request,'hospital/admin_dashboard.html',context=mydict)


#this view for sidebar click on admin page
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_doctor_view(request):
    return render(request,'hospital/admin_doctor.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_lab_tech_view(request):
    return render(request,'hospital/admin_lab_tech.html')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_hospital_view(request):
     return render(request,'hospital/admin_hospital.html')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_doctor_view(request):
    doctors=models.Doctor.objects.all().filter(status=True)
    return render(request,'hospital/admin_view_doctor.html',{'doctors':doctors})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_lab_tech_view(request):
    lab_techs=models.LabTech.objects.all().filter(status=True)
    return render(request,'hospital/admin_view_lab_tech.html',{'lab_techs':lab_techs})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_schedule_doctor_view(request):
    doctors=models.Doctor.objects.all().filter(status=True)
    return render(request,'hospital/admin_view_doctor_scheduling.html',{'doctors':doctors})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def scheduling_doctor_view(request,pk):
    doctor=models.Doctor.objects.get(id=pk)
    user=models.User.objects.get(id=doctor.user_id)
    userForm=forms.DoctorUserForm(instance=user)
    doctorForm=forms.DoctorForm(request.FILES,instance=doctor)
    mydict={'userForm':userForm,'doctorForm':doctorForm}
    if request.method=='POST':
        doctorScheduling=models.ScheduleAppointment()
        doctorScheduling.morning_1 = request.POST.get('morning_1')
        doctorScheduling.morning_2 = request.POST.get('morning_2')
        doctorScheduling.morning_3 = request.POST.get('morning_3')
        doctorScheduling.morning_4 = request.POST.get('morning_4')
        doctorScheduling.morning_5 = request.POST.get('morning_5')
        doctorScheduling.morning_6 = request.POST.get('morning_6')
        doctorScheduling.morning_7 = request.POST.get('morning_7')
        doctorScheduling.morning_8 = request.POST.get('morning_8')
        doctorScheduling.morning_9 = request.POST.get('morning_9')
        doctorScheduling.morning_10 = request.POST.get('morning_10')
        doctorScheduling.morning_11 = request.POST.get('morning_11')
        doctorScheduling.morning_12 = request.POST.get('morning_12')

        doctorScheduling.afternoon_1 = request.POST.get('afternoon_1')
        doctorScheduling.afternoon_2 = request.POST.get('afternoon_2')
        doctorScheduling.afternoon_3 = request.POST.get('afternoon_3')
        doctorScheduling.afternoon_4 = request.POST.get('afternoon_4')
        doctorScheduling.afternoon_5 = request.POST.get('afternoon_5')
        doctorScheduling.afternoon_6 = request.POST.get('afternoon_6')
        doctorScheduling.afternoon_7 = request.POST.get('afternoon_7')
        doctorScheduling.afternoon_8 = request.POST.get('afternoon_8')
        doctorScheduling.afternoon_9 = request.POST.get('afternoon_9')
        doctorScheduling.afternoon_10 = request.POST.get('afternoon_10')
        doctorScheduling.afternoon_11 = request.POST.get('afternoon_11')
        doctorScheduling.afternoon_12 = request.POST.get('afternoon_12')

        doctorScheduling.evening_1 = request.POST.get('evening_1')
        doctorScheduling.evening_2 = request.POST.get('evening_2')
        doctorScheduling.evening_3 = request.POST.get('evening_3')
        doctorScheduling.evening_4 = request.POST.get('evening_4')
        doctorScheduling.evening_5 = request.POST.get('evening_5')
        doctorScheduling.evening_6 = request.POST.get('evening_6')
        doctorScheduling.evening_7 = request.POST.get('evening_7')
        doctorScheduling.evening_8 = request.POST.get('evening_8')
        doctorScheduling.evening_9 = request.POST.get('evening_9')
        doctorScheduling.evening_10 = request.POST.get('evening_10')
        doctorScheduling.evening_11 = request.POST.get('evening_11')
        doctorScheduling.evening_12 = request.POST.get('evening_12')
        doctorScheduling.doctorId=doctor.user.id 
        doctorScheduling.doctorName=doctor.user.first_name
        doctorScheduling.doctorDepartment=doctor.department
        doctorScheduling.save()

        doctor.is_avialable=True
        doctor.save()

        return redirect('admin-view-doctor-scheduled')
    return render(request,'hospital/admin_doctor_scheduling.html',context=mydict)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_scheduled_doctor_view(request):

    scheduledDoctor=models.ScheduleAppointment.objects.all()
    return render(request,'hospital/admin_view_scheduled_doctor.html',{'scheduledDoctor':scheduledDoctor})



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_hospital_view(request):
     hospitals=models.Hospital.objects.all()
     return render(request,'hospital/admin_view_hospital.html',{'hospitals':hospitals})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_doctor_from_hospital_view(request, pk):
    if request.method == 'POST':
        doctor = models.Doctor.objects.get(id=pk)
        user = models.User.objects.get(id=doctor.user_id)
        if 'confirm_delete' in request.POST:
            user.delete()
            doctor.delete()
            return redirect('admin-view-doctor')
        else:
            return redirect('admin-view-doctor')  # Redirect to the doctor's view page or wherever you need
        
    return render(request, 'hospital/confirm_delete.html')  # Assuming you have a template named 'confirm_delete.html' for confirmation

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def update_doctor_view(request,pk):
    doctor=models.Doctor.objects.get(id=pk)
    user=models.User.objects.get(id=doctor.user_id)

    userForm=forms.DoctorUserForm(instance=user)
    doctorForm=forms.DoctorForm(request.FILES,instance=doctor)
    mydict={'userForm':userForm,'doctorForm':doctorForm}
    if request.method=='POST':
        userForm=forms.DoctorUserForm(request.POST,instance=user)
        doctorForm=forms.DoctorForm(request.POST,request.FILES,instance=doctor)
        if userForm.is_valid() and doctorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            doctor=doctorForm.save(commit=False)
            doctor.status=True
            doctor.save()
            return redirect('admin-view-doctor')
    return render(request,'hospital/admin_update_doctor.html',context=mydict)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_doctor_view(request):

    if request.method=='POST':
        userForm=forms.DoctorUserForm(request.POST)
        doctorForm=forms.DoctorForm(request.POST, request.FILES)
        if userForm.is_valid() and doctorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()

            doctor=doctorForm.save(commit=False)
            doctor.user=user
            doctor.hospital_name=request.POST.get('hospital_Id')
            doctor.admitDate=date.today()
            doctor.status=True
            doctor.save()

            my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group[0].user_set.add(user)
            

            return HttpResponseRedirect('admin-view-doctor')
    else:
        userForm=forms.DoctorUserForm()
        doctorForm=forms.DoctorForm()
    mydict={'userForm':userForm,'doctorForm':doctorForm}        
    return render(request,'hospital/admin_add_doctor.html',context=mydict)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_lab_tech_view(request):

    if request.method=='POST':
        userForm=forms.Lab_TechUserForm(request.POST)
        lab_techForm=forms.Lab_TechForm(request.POST, request.FILES)
        if userForm.is_valid() and lab_techForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            lab_tech=lab_techForm.save(commit=False)
            lab_tech.user=user
            lab_tech.hospital_name=request.POST.get('hospital_Id')
            lab_tech.status=True
            lab_tech.save()

            my_lab_tech_group = Group.objects.get_or_create(name='LAB_TECH')
            my_lab_tech_group[0].user_set.add(user)

            return HttpResponseRedirect('admin-view-lab_tech')
    else:
        userForm=forms.Lab_TechUserForm()
        lab_techForm=forms.Lab_TechForm()
    mydict={'userForm':userForm,'lab_techForm':lab_techForm} 
    return render(request,'hospital/admin_add_lab_tech.html',context=mydict)

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_hospital_view(request):

    if request.method=='POST':
        hospitalForm=forms.HospitalForm(request.POST,request.FILES)
        if hospitalForm.is_valid():
            hospital=hospitalForm.save()
            hospital.hospitalId=models.Hospital.objects.all().count()+1
            hospital.save()
            return HttpResponseRedirect('admin-view-hospital')
    else:
        hospitalForm=forms.HospitalForm()

    mydict={'hospitalForm':hospitalForm}
    return render(request,'hospital/admin_add_hospital.html',context=mydict)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_hospital_view(request,pk):
    hospital=models.Hospital.objects.get(id=pk)
    hospital.delete()
    return redirect('admin-view-hospital')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def update_hospital_view(request,pk):
    hospital=models.Hospital.objects.get(id=pk)
    hospitalForm=forms.HospitalForm(request.FILES,instance=hospital)
    mydict={'hospitalForm':hospitalForm}
    if request.method=='POST':
        hospitalForm=forms.HospitalForm(request.POST,request.FILES,instance=hospital)
        if hospitalForm.is_valid():
            hospital=hospitalForm.save(commit=False)
            hospital.save()
            return redirect('admin-view-hospital')
    return render(request,'hospital/admin_update_hospital.html',context=mydict)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_doctor_specialisation_view(request):
    doctors=models.Doctor.objects.all().filter(status=True)
    return render(request,'hospital/admin_view_doctor_specialisation.html',{'doctors':doctors})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_doctor_certification_view(request,pk):
    certificates=models.Doctor.objects.get(status=True,id=pk)
    certificate=models.Doctor.objects.all().filter(id=pk)
    return render(request,'hospital/admin_view_doctor_certification.html',{'certificates':certificates,'certificate':certificate})



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_patient_view(request):
    return render(request,'hospital/admin_patient.html')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_patient_view(request):
    patients=models.Patient.objects.all().filter(status=True)
    return render(request,'hospital/admin_view_patient.html',{'patients':patients})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_patient_from_hospital_view(request,pk):
    patient=models.Patient.objects.get(id=pk)
    user=models.User.objects.get(id=patient.user_id)
    user.delete()
    patient.delete()
    return redirect('admin-view-patient')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def update_patient_view(request,pk):
    patient=models.Patient.objects.get(id=pk)
    user=models.User.objects.get(id=patient.user_id)

    userForm=forms.PatientUserForm(instance=user)
    patientForm=forms.PatientForm(request.FILES,instance=patient)
    mydict={'userForm':userForm,'patientForm':patientForm}
    if request.method=='POST':
        userForm=forms.PatientUserForm(request.POST,instance=user)
        patientForm=forms.PatientForm(request.POST,request.FILES,instance=patient)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            patient=patientForm.save(commit=False)
            patient.status=True
            patient.save()
            return redirect('admin-view-patient')
    return render(request,'hospital/admin_update_patient.html',context=mydict)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_patient_view(request):

    if request.method=='POST':
        userForm=forms.PatientUserForm(request.POST)
        patientForm=forms.PatientForm(request.POST,request.FILES)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()

            patient=patientForm.save(commit=False)
            patient.user=user
            patient.status=True
            patient.save()

            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)
            return HttpResponseRedirect('admin-view-patient')
    else:
        userForm=forms.PatientUserForm()
        patientForm=forms.PatientForm()
    mydict={'userForm':userForm,'patientForm':patientForm}
    return render(request,'hospital/admin_add_patient.html',context=mydict)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_pharmacist_view(request):

    if request.method=='POST':
        userForm=forms.PharmacistUserForm(request.POST)
        pharmacistForm=forms.PharmacistForm(request.POST, request.FILES)
        if userForm.is_valid() and pharmacistForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()

            pharmacist=pharmacistForm.save(commit=False)
            pharmacist.user=user
            pharmacist.hospital_name=request.POST.get('hospital_Id')
            pharmacist.status=True
            pharmacist.save()

            my_pharmacist_group = Group.objects.get_or_create(name='PHARMACIST')
            my_pharmacist_group[0].user_set.add(user)

            return HttpResponseRedirect('admin-view-pharmacist')
    else:
        userForm=forms.PharmacistUserForm()
        pharmacistForm=forms.PharmacistForm()
    mydict={'userForm':userForm,'pharmacistForm':pharmacistForm}
    return render(request,'hospital/admin_add_pharmacist.html',context=mydict)


@login_required(login_url='pharmacistlogin')
@user_passes_test(is_pharmacist)
def pharmacist_add_medicine_view(request):
    pharmacist = models.Pharmacist.objects.get(user_id=request.user.id)  # for profile picture of  in sidebar
    
    if request.method == 'POST':
        medicineForm = forms.MedicineForm(request.POST, request.FILES)
        if medicineForm.is_valid():
            medicine = medicineForm.save(commit=False)
            medicine.status = True
            medicine.save()
            return HttpResponseRedirect('pharmacist-view-medicine')
    else:
        medicineForm = forms.MedicineForm()
        
    mydict = {'medicineForm': medicineForm, 'pharmacist': pharmacist}
    return render(request, 'hospital/pharmacist_add_medicine.html', context=mydict)


@login_required(login_url='pharmacistlogin')
@user_passes_test(is_pharmacist)
def pharmacist_view_medicine_view(request):
    pharmacist=models.Pharmacist.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    medicines=models.Medicine.objects.all().filter(status=True)
    return render(request,'hospital/pharmacist_view_medicine.html',{'medicines':medicines,'pharmacist':pharmacist})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_pharmacist_view(request):
    return render(request,'hospital/admin_pharmacist.html')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_pharmacist_view(request):
    pharmacists=models.Pharmacist.objects.all().filter(status=True)
    return render(request,'hospital/admin_view_pharmacist.html',{'pharmacists':pharmacists})


#------------------FOR APPROVING PATIENT BY ADMIN----------------------

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_approve_patient_view(request):
    #those whose approval are needed
    patients=models.Patient.objects.all().filter(status=False)
    return render(request,'hospital/admin_approve_patient.html',{'patients':patients})


#------------------notification view---------------------

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_notification_view(request):
    patients=models.Patient.objects.all().filter(status=False)
    return render(request,'hospital/admin_notification.html',{'patients':patients})


@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_notification_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    pendingappointmentcount=models.Appointment.objects.all().filter(status=False,doctorId=request.user.id).count()
    patientlabresult=models.PatientLabResult.objects.all().filter(doctorName=request.user.first_name)
    patientlabresultcount=models.PatientLabResult.objects.all().filter(doctorId=request.user.id).count()
    appointments=models.Appointment.objects.all().filter(status=False)
    return render(request,'hospital/doctor_notification.html',{'appointments':appointments,'pendingappointmentcount':pendingappointmentcount,'patientlabresult':patientlabresult,'patientlabresultcount':patientlabresultcount,'doctor':doctor})


@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_notification_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    labPaymentRequest=models.LabTechRequestPayment.objects.all().filter(status=False,patientName=request.user.first_name).count()
    medicinePaymentRequest=models.PharmacistRequestPayment.objects.all().filter(status=False,patientName=request.user.first_name).count()
    announcementFromDoctor=models.Announcement.objects.all().filter(patientId=request.user.id)
    return render(request,'hospital/patient_notification.html',{'labPaymentRequest':labPaymentRequest,'medicinePaymentRequest':medicinePaymentRequest,'announcementFromDoctor':announcementFromDoctor,'patient':patient})


@login_required(login_url='labTechlogin')
@user_passes_test(is_lab_tech)
def labTech_notification_view(request):
    labtech=models.LabTech.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    laborders=models.Laboratory.objects.all().filter(status=True,labTechName=request.user.first_name)
    patientPayementSuccess=models.LabTechRequestPayment.objects.all().filter(status=True,labTechName=request.user.first_name)
    patientPayementSuccesscount=models.LabTechRequestPayment.objects.all().filter(status=True,labTechName=request.user.first_name).count()
    labOrdercount=models.Laboratory.objects.all().filter(status=True,labTechName=request.user.first_name).count()
    return render(request,'hospital/labTech_notification.html',{'patientPayementSuccesscount':patientPayementSuccesscount,'labOrdercount':labOrdercount,'laborders':laborders,'patientPayementSuccess':patientPayementSuccess,'labtech':labtech})


@login_required(login_url='pharmacistlogin')
@user_passes_test(is_pharmacist)
def pharmacist_notification_view(request):
    pharmacist=models.Pharmacist.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    prescriptionorders=models.Prescription.objects.all().filter(status=True,pharmacistId=request.user.id)
    patientPayementSuccess=models.PharmacistRequestPayment.objects.all().filter(status=True,pharmacistId=request.user.id)
    patientPayementSuccesscount=models.PharmacistRequestPayment.objects.all().filter(status=True,pharmacistId=request.user.id).count()
    prescriptionordercount=models.Prescription.objects.all().filter(status=True,pharmacistId=request.user.id).count()
    return render(request,'hospital/pharmacist_notification.html',{'patientPayementSuccesscount':patientPayementSuccesscount,'prescriptionordercount':prescriptionordercount,'prescriptionorders':prescriptionorders,'patientPayementSuccess':patientPayementSuccess,'pharmacist':pharmacist})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def approve_patient_view(request,pk):
    patient=models.Patient.objects.get(id=pk)
    patient.status=True
    patient.save()
    return redirect(reverse('admin-approve-patient'))



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def reject_patient_view(request,pk):
    patient=models.Patient.objects.get(id=pk)
    user=models.User.objects.get(id=patient.user_id)
    user.delete()
    patient.delete()
    return redirect('admin-approve-patient')

#----------profile-----------------

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_profile_view(request):
    adminProfile=models.User.objects.all().filter(username=request.user.username)

    return render(request,'hospital/admin_profile_view.html',{'adminProfile':adminProfile})

@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_profile_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    doctorProfile=models.Doctor.objects.all().filter(status=True,user_id=request.user.id)

    return render(request,'hospital/doctor_profile_view.html',{'doctorProfile':doctorProfile,'doctor':doctor})


@login_required(login_url='labTechlogin')
@user_passes_test(is_lab_tech)
def labTech_profile_view(request):
    labtech=models.LabTech.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    labTechProfile=models.LabTech.objects.all().filter(status=True,user_id=request.user.id)

    return render(request,'hospital/labTech_profile_view.html',{'labTechProfile':labTechProfile,'labtech':labtech})

@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_profile_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture   in sidebar
    patientProfile=models.Patient.objects.all().filter(status=True,user_id=request.user.id)

    return render(request,'hospital/patient_profile_view.html',{'patientProfile':patientProfile,'patient':patient})


@login_required(login_url='pharmacistlogin')
@user_passes_test(is_pharmacist)
def pharmacist_profile_view(request):
    pharmacist=models.Pharmacist.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    pharmacistProfile=models.Pharmacist.objects.all().filter(status=True,user_id=request.user.id)

    return render(request,'hospital/pharmasict_profile_view.html',{'pharmacistProfile':pharmacistProfile,'pharmacist':pharmacist})


#-----------------Laboratory START--------------------------------------------------------------------

@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_laboratory_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    return render(request,'hospital/doctor_laboratory.html',{'doctor':doctor})


@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_order_Lab_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    if request.method=='POST':
        sample=models.Laboratory()
        sample.sampleType = request.POST.get('selectedlabtest')
        sample.amount = request.POST.get('amount')
        sample.labTechName = request.POST.get('labTechName')
        sample.patientName = request.POST.get('patientName')
        sample.orderDate = request.POST.get('orderDate')
        sample.doctorName=request.user.first_name
        sample.doctorId=request.user.id
        sample.user_id=request.user.id
        sample.status=True
        sample.save()
        return HttpResponseRedirect('doctor-view-labOrder')
    else:
        mydict={'doctor':doctor}
    return render(request,'hospital/doctor_order_lab.html',context=mydict)


@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_view_labOrder_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    laboratorys=models.Laboratory.objects.all().filter(doctorId=request.user.id).order_by('-id')
    return render(request,'hospital/doctor_view_labOrder.html',{'laboratorys':laboratorys,'doctor':doctor})


#----------symptoms-----------------

@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_view_patient_symptom_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    symptoms=models.Symptom.objects.all().filter(status=True).order_by('-id')
    return render(request,'hospital/doctor_view_patient_symptom.html',{'symptoms':symptoms,'doctor':doctor})

@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_view_sy_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    appointments=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id)
    smid=[]
    for a in appointments:
        smid.append(a.patientId)
    symptoms=models.Symptom.objects.all().filter(status=True,symptomId__in=smid)
    appointments=zip(appointments,symptoms)
    return render(request,'hospital/doctor_view_patient_symptom.html',{'appointments':appointments,'doctor':doctor})


#-----------------Announcement --------------------------------------------------------------------

@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_announcement_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    return render(request,'hospital/doctor_announcement.html',{'doctor':doctor})

@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_post_announcement_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    announcementForm=forms.AnnouncementForm()
    if request.method=='POST':
        announcementForm=forms.AnnouncementForm(request.POST)
        if announcementForm.is_valid():
            announcement=announcementForm.save(commit=False)
            announcement.doctorId=request.user.id
            announcement.patientId=request.POST.get('patientId')
            announcement.patientName=models.User.objects.get(id=request.POST.get('patientId')).first_name
            announcement.doctorName=request.user.first_name
            announcement.save()
            return HttpResponseRedirect('doctor-view-announcement')
    else:
        announcementForm=forms.AnnouncementForm()

    mydict={'announcementForm':announcementForm,'doctor':doctor}

    return render(request,'hospital/doctor_post_announcement.html',context=mydict)

@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_view_announcement_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    announcements=models.Announcement.objects.all().filter(doctorId=request.user.id).order_by('id')
    return render(request,'hospital/doctor_view_announcement.html',{'announcements':announcements,'doctor':doctor})

@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def delete_posted_announcement_view(request, pk):
        announcement = models.Announcement.objects.get(id=pk) 
        announcement.delete()
        return redirect('doctor-view-announcement')
      

#-----------------Prescription --------------------------------------------------------------------

@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_prescription_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    return render(request,'hospital/doctor_prescription.html',{'doctor':doctor})

@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_give_prescription_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    patient_id=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id)
    prescriptionForm=forms.PrescriptionForm()
    if request.method=='POST':
        prescriptionForm=forms.PrescriptionForm(request.POST)
        if prescriptionForm.is_valid():
            prescription=prescriptionForm.save(commit=False)
            prescription.doctorId=request.user.id
            prescription.pharmacistId=request.POST.get('pharmacistId')
            prescription.pharmacistName=models.User.objects.get(id=request.POST.get('pharmacistId')).first_name
            prescription.status=True
            prescription.save()
            return HttpResponseRedirect('doctor-view-prescription')
    else:
        prescriptionForm=forms.PrescriptionForm()

    mydict={'prescriptionForm':prescriptionForm,'patient_id':patient_id,'doctor':doctor}

    return render(request,'hospital/doctor_give_prescription.html',context=mydict)

@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_view_prescription_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    prescriptions=models.Prescription.objects.all().filter(status=True).order_by('-id')
    return render(request,'hospital/doctor_view_prescription.html',{'prescriptions':prescriptions,'doctor':doctor})

@login_required(login_url='pharmacistlogin')
@user_passes_test(is_pharmacist)
def pharmacist_prescription_view(request):
    pharmacist=models.Pharmacist.objects.get(user_id=request.user.id) #for profile picture in sidebar
    return render(request,'hospital/pharmacist_prescription.html',{'pharmacist':pharmacist})

@login_required(login_url='pharmacistlogin')
@user_passes_test(is_pharmacist)
def pharmacist_view_prescription_view(request):
    pharmacist=models.Pharmacist.objects.get(user_id=request.user.id) #for profile picture  in sidebar
    prescriptions=models.Prescription.objects.all().filter(status=True,pharmacistId=request.user.id).order_by('-id')
    return render(request,'hospital/pharmacist_view_prescription.html',{'prescriptions':prescriptions,'pharmacist':pharmacist})


#----------request payment-----------------

@login_required(login_url='pharmacistlogin')
@user_passes_test(is_pharmacist)
def pharmacist_request_payment_view(request,pk):
    pharmacist=models.Pharmacist.objects.get(user_id=request.user.id) #for profile picture  in sidebar
    patient=models.Prescription.objects.get(id=pk)
    prescriptionForm=forms.PrescriptionForm(instance=patient)
    payementRequestForm=forms.PharmacistRequestPaymentForm()
    mydict={'prescriptionForm':prescriptionForm,'payementRequestForm':payementRequestForm,'pharmacist':pharmacist}
    if request.method=='POST':
        payementRequestForm=forms.PharmacistRequestPaymentForm(request.POST)
        if payementRequestForm.is_valid():
            paymentRequest=payementRequestForm.save(commit=False)
            paymentRequest.status=False
            paymentRequest.pharmacistName=request.user.first_name
            paymentRequest.hospitalName= models.Pharmacist.objects.get(user_id=request.user.id).hospital_name
            paymentRequest.patientId=models.LabTechRequestPayment.objects.all().count()+1
            paymentRequest.pharmacistId=request.user.id
            paymentRequest.save()
            return redirect('pharmacist-view-paymentRequest')
    return render(request,'hospital/pharmacist_request_payment.html',context=mydict)

@login_required(login_url='pharmacistlogin')
@user_passes_test(is_pharmacist)
def pharmacist_view_paymentRequest_view(request):
    pharmacist=models.Pharmacist.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    paymentRequests=models.PharmacistRequestPayment.objects.all().filter(pharmacistId=request.user.id)
    return render(request,'hospital/pharmacist_view_paymentRequest.html',{'paymentRequests':paymentRequests,'pharmacist':pharmacist})


@login_required(login_url='pharmacistlogin')
@user_passes_test(is_pharmacist)
def pharmacist_view_paymentRequest_status_view(request):
    pharmacist=models.Pharmacist.objects.get(user_id=request.user.id) #for profile picture in sidebar
    paymentRequests=models.PharmacistRequestPayment.objects.all().filter(pharmacistId=request.user.id)
    return render(request,'hospital/pharmasict_view_paymentRequest_status.html',{'paymentRequests':paymentRequests,'pharmacist':pharmacist})


@login_required(login_url='pharmacistlogin')
@user_passes_test(is_pharmacist)
def pharmacist_patient_view(request):
    pharmacist=models.Pharmacist.objects.get(user_id=request.user.id) #for profile picture in sidebar
    return render(request,'hospital/pharmasict_patient.html',{'pharmacist':pharmacist})


@login_required(login_url='pharmacistlogin')
@user_passes_test(is_pharmacist)
def pharmacist_view_payed_patient_to_give_instruction_view(request):
    pharmacist=models.Pharmacist.objects.get(user_id=request.user.id) #for profile picture in sidebar
    payedPatient=models.PharmacistRequestPayment.objects.all().filter(status=True,pharmacistId=request.user.id)
    return render(request,'hospital/pharmacist_view_payed_patient_to_give_instruction.html',{'payedPatient':payedPatient,'pharmacist':pharmacist})


@login_required(login_url='labTechlogin')
@user_passes_test(is_lab_tech)
def labTech_request_payment_view(request,pk):
    labtech=models.LabTech.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    patient=models.Laboratory.objects.get(id=pk)
    user=models.User.objects.get(id=patient.user_id)
    userForm=forms.PatientUserForm(instance=user)
    labOrderForm=forms.LaboratoryForm(instance=patient)
    mydict={
        'labOrderForm':labOrderForm,
        'labtech':labtech,        
        'amount':patient.amount,
        'sampleType':patient.sampleType,
        'patientName':patient.patientName,
        'doctorName':patient.doctorName,
        'orderDate':patient.orderDate,
        }
    if request.method=='POST':
            paymentrequest=models.LabTechRequestPayment()
            paymentrequest.sampleType = request.POST.get('sampleType')
            paymentrequest.testPrice = request.POST.get('amount')
            paymentrequest.patientName = request.POST.get('patientName')
            paymentrequest.orderDate = request.POST.get('orderDate')
            paymentrequest.doctorName=request.POST.get('doctorName')
            paymentrequest.description=request.POST.get('description')
            paymentrequest.labTechName=request.user.first_name
            paymentrequest.hospitalName= models.LabTech.objects.get(user_id=request.user.id).hospital_name
            paymentrequest.patientId=models.LabTechRequestPayment.objects.all().count()+1
            paymentrequest.labTechId=request.user.id
            paymentrequest.status=False
            paymentrequest.save()
            return redirect('labTech-view-labRequest')
    else:
            print('wrong....')
    return render(request,'hospital/labTech_request_payment.html',context=mydict)


@login_required(login_url='labTechlogin')
@user_passes_test(is_lab_tech)
def labTech_view_labRequest_view(request):
    labtech=models.LabTech.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    labRequests=models.LabTechRequestPayment.objects.all().filter(labTechId=request.user.id)
    return render(request,'hospital/labTech_view_labRequest.html',{'labRequests':labRequests,'labtech':labtech})


@login_required(login_url='labTechlogin')
@user_passes_test(is_lab_tech)
def labTech_view_labRequest_status_view(request):
    labtech=models.LabTech.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    labRequests=models.LabTechRequestPayment.objects.all().filter(labTechId=request.user.id)
    return render(request,'hospital/labTech_view_labRequest_status.html',{'labRequests':labRequests,'labtech':labtech})


#-----------------Medicine --------------------------------------------------------------------

@login_required(login_url='pharmacistlogin')
@user_passes_test(is_pharmacist)
def pharmacist_medicine_view(request):
    pharmacist=models.Pharmacist.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    return render(request,'hospital/pharmacist_medicine.html',{'pharmacist':pharmacist})

@login_required(login_url='pharmacistlogin')
@user_passes_test(is_pharmacist)
def pharmacist_view_medicine_instruction_view(request):
    pharm=models.Pharmacist.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    instructions=models.PatientMedicineInstruction.objects.all().filter(status=True,pharmacistId=request.user.id)#??????? change to id
    return render(request,'hospital/pharmacist_view_medicine_instruction.html',{'instructions':instructions,'pharm':pharm})


@login_required(login_url='pharmacistlogin')
@user_passes_test(is_pharmacist)
def pharmacist_give_medicine_instruction_view(request,pk):
    pharmacist=models.Pharmacist.objects.get(user_id=request.user.id) #for profile picture  in sidebar
    patient=models.PharmacistRequestPayment.objects.get(id=pk)
    paymentForm=forms.PharmacistRequestPaymentForm(instance=patient)
    giveMedicineInstructionForm=forms.PharmacistGiveMedicineInstructionForm()
    mydict={'paymentForm':paymentForm,'giveMedicineInstructionForm':giveMedicineInstructionForm,'pharmacist':pharmacist}
    if request.method=='POST':
        giveMedicineInstructionForm=forms.PharmacistGiveMedicineInstructionForm(request.POST)
        if giveMedicineInstructionForm.is_valid():
            giveInstruction=giveMedicineInstructionForm.save(commit=False)
            giveInstruction.status=True
            giveInstruction.pharmacistName=request.user.first_name
            giveInstruction.patientId=models.PatientMedicineInstruction.objects.all().count()+1
            giveInstruction.pharmacistId=request.user.id
            giveInstruction.save()
            return redirect('pharmacist-view-instruction')
        else:
            print('invalid')
    return render(request,'hospital/pharmacist_give_medicine_instruction.html',context=mydict)


@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_read_instruction_to_use_medicine(request):
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    readInstructions=models.PatientMedicineInstruction.objects.all().filter(status=True,patientName=request.user.first_name)#??????? change to id
    return render(request,'hospital/patient_read_instruction_to_use_medicine.html',{'readInstructions':readInstructions,'patient':patient})



#-----------------APPOINTMENT --------------------------------------------------------------------

@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_appointment_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    return render(request,'hospital/doctor_appointment.html',{'doctor':doctor})


@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_view_appointment_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    totalappointement=models.Appointment.objects.all().filter(status=True ,doctorId=request.user.id).count()
    appointments=models.Appointment.objects.all().filter(status=True)
    return render(request,'hospital/doctor_view_appointment.html',{'appointments':appointments,'totalappointement':totalappointement,'doctor':doctor})


@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_add_appointment_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    appointmentForm=forms.AppointmentForm()
    mydict={'appointmentForm':appointmentForm,'doctor':doctor}
    if request.method=='POST':
        appointmentForm=forms.AppointmentForm(request.POST)
        if appointmentForm.is_valid():
            appointment=appointmentForm.save(commit=False)
            appointment.doctorId=request.POST.get('doctorId')
            appointment.patientId=request.POST.get('patientId')
            appointment.doctorName=models.User.objects.get(id=request.POST.get('doctorId')).first_name
            appointment.patientName=models.User.objects.get(id=request.POST.get('patientId')).first_name
            appointment.status=True
            appointment.save()
        return HttpResponseRedirect('doctor-view-appointment')
    return render(request,'hospital/doctor_add_appointment.html',context=mydict)



@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_approve_appointment_view(request):
    #those whose approval are needed
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    appointments=models.Appointment.objects.all().filter(status=False)
    return render(request,'hospital/doctor_approve_appointment.html',{'appointments':appointments,'doctor':doctor})


@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def approve_appointment_view(request,pk):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    appointment=models.Appointment.objects.get(id=pk)
    appointment.status=True
    appointment.save()
    return redirect('doctor-view-appointment')


@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def reject_appointment_view(request,pk):
    appointment=models.Appointment.objects.get(id=pk)
    appointment.delete()
    return redirect('doctor-approve-appointment')

@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def discharge_patient(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    appointments=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id).order_by('-id')
    patientid=[]
    for a in appointments:
        patientid.append(a.patientId)
    patients=models.Patient.objects.all().filter(status=True,user_id__in=patientid).order_by('-id')
    appointments=zip(appointments,patients)
    return render(request,'hospital/doctor_discharge_patient.html',{'doctor':doctor,'appointments':appointments})



@login_required(login_url='labTechlogin')
@user_passes_test(is_lab_tech)
def labTech_dashboard_view(request):
    labResultcount=models.PatientLabResult.objects.all().filter(labTechId=request.user.id).count()
    patientPayementSuccesscount=models.LabTechRequestPayment.objects.all().filter(status=True,labTechId=request.user.id).count()
    labOrdercount=models.Laboratory.objects.all().filter(status=True,labTechId=request.user.id).count()
    notificationcount=int(patientPayementSuccesscount + labOrdercount)    
    labOrders=models.Laboratory.objects.all().filter(status=True,labTechId=request.user.id).order_by('-id')   
    mydict = {
        'labtech':models.LabTech.objects.get(user_id=request.user.id), #for profile picture of doctor in sidebar
        'labResultcount':labResultcount,
        'labOrdercount':labOrdercount,
        'labOrders':labOrders,
        'notificationcount':notificationcount,
    

    }
   
    return render(request,'hospital/labTech_dashboard.html',context=mydict)


@login_required(login_url='labTechlogin')
@user_passes_test(is_lab_tech)
def labTech_patient_view(request):
    labtech=models.LabTech.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    return render(request,'hospital/labTech_patient.html',{'labtech':labtech})

@login_required(login_url='labTechlogin')
@user_passes_test(is_lab_tech)
def labTech_view_report_labResult(request):
    labtech=models.LabTech.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    patients=models.LabTechRequestPayment.objects.all().filter(status=True,labTechId=request.user.id)
    return render(request,'hospital/labTech_report_lab_result.html',{'patients':patients,'labtech':labtech})

@login_required(login_url='labTechlogin')
@user_passes_test(is_lab_tech)
def labTech_report_patient_labResult(request,pk):
    labtech=models.LabTech.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    patient=models.LabTechRequestPayment.objects.get(id=pk)
    labRequestForm=forms.LabTechRequestPaymentForm(instance=patient)
    labResultForm=forms.PatientLabResultForm()
    mydict={'labResultForm':labResultForm,'labRequestForm':labRequestForm,'labtech':labtech}
    if request.method=='POST':
        labResultForm=forms.PatientLabResultForm(request.POST)
        if labResultForm.is_valid():
            labResult=labResultForm.save(commit=False)
            labResult.labTechName=request.user.first_name
            labResult.patientId=models.PatientLabResult.objects.all().count()+1
            labResult.labTechId=request.user.id
            labResult.save()
            return redirect('labTech-view-labResult')
        else:
            print('invalid')
    return render(request,'hospital/labTech_report_patient_labResult.html',context=mydict)


@login_required(login_url='labTechlogin')
@user_passes_test(is_lab_tech)
def labTech_view_reported_patient_labResult(request):
    labtech=models.LabTech.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    patients=models.PatientLabResult.objects.all().filter(labTechId=request.user.id)
    return render(request,'hospital/labTech_view_report_labResult.html',{'patients':patients,'labtech':labtech})


@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_view_labRequest_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    labRequests=models.LabTechRequestPayment.objects.all().filter(status=False,patientName=request.user.first_name)#??????? change to id
    return render(request,'hospital/patient_view_labRequest.html',{'labRequests':labRequests,'patient':patient})

@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_view_medicine_view(request):

    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    paymentRequests=models.PharmacistRequestPayment.objects.all().filter(status=False,patientName=request.user.first_name)#??????? change to id

    return render(request,'hospital/patient_view_medicine.html',{'paymentRequests':paymentRequests,'patient':patient})


@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_payment_view(request):
    
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    return render(request,'hospital/patient_payment.html',{'patient':patient})

@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_view_symptom_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    symptoms=models.DoctorRecommondation.objects.all().filter(patent_Id=request.user.id)
    return render(request,'hospital/patient_view_symptom.html',{'symptoms':symptoms,'patient':patient})


@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_medicalRecord_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    return render(request,'hospital/patient_medicalRecord.html',{'patient':patient})


@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_view_payment_method_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
        
    return render(request,'hospital/patient_choose_payment_method.html',{'patient':patient})


def patient_view_generate_bill_view(request,pk):
    patient=models.LabTechRequestPayment.objects.get(id=pk)
    patient.status=True
    patient.save()
    labTechId=models.User.objects.all().filter(id=patient.labTechId)
    receiverName="CompanyOfEhospitalForHararCity"
    receiveraccount="1000275541078"
    transactionId="FT248056HqR"
    transactionId=transactionId+""+str(models.PatientPayementDetail.objects.all().count()+1)
    patientDict={
        'patientId':pk,
        'labTechName':labTechId[0].first_name,
        'receiver':receiverName,
        'receiverAccount':receiveraccount,
        'transactionId':transactionId,
        'paymentDate':date.today(),
        'paymentTime':datetime.now(),
        'amount':patient.testPrice,
        'patient':models.Patient.objects.get(user_id=request.user.id),
    }
    if request.method == 'POST':
        feeDict ={
            'fullName':request.POST['fullName'],
            'email':request.POST['email'],
            'phone':request.POST['phone'],
            'total':(int(request.POST['amount']))
        }
        patientDict.update(feeDict)
       
        #for updating to database patientpaymentDetails (ppD)
        ppD=models.PatientPayementDetail()
        ppD.patientId=pk
        ppD.fullName=request.POST['fullName']
        ppD.email=request.POST['email']
        ppD.phone=request.POST['phone']
        ppD.receiver=receiverName
        ppD.receiverAccount=receiveraccount
        ppD.transactionId=transactionId
        ppD.paymentDate=date.today()
        ppD.paymentTime=datetime.now()
        ppD.amount=patient.testPrice
        ppD.total=(int(request.POST['amount']))
        ppD.save()
        print(feeDict)
        return render(request,'hospital/patient_final_bill.html',context=patientDict)
    return render(request,'hospital/patient_generate_bill.html',context=patientDict)



def patient_view_generate_bill_forMedicine_view(request,pk):
    patient=models.PharmacistRequestPayment.objects.get(id=pk)
    pharmacistId=models.User.objects.all().filter(id=patient.pharmacistId)
    receiverName="CompanyOfEhospitalForHararCity"
    receiveraccount="1000275541078"
    transactionId="FT248056HqR"
    transactionId=transactionId+""+str(models.PatientPayementDetail.objects.all().count()+1)
    patientDict={
        'patientId':pk,
        'pharmacistName':pharmacistId[0].first_name,
        'receiver':receiverName,
        'receiverAccount':receiveraccount,
        'transactionId':transactionId,
        'paymentDate':date.today(),
        'paymentTime':datetime.now(),
        'amount':patient.medicinePrice,
        'patient':models.Patient.objects.get(user_id=request.user.id),
    }
    if request.method == 'POST':
        feeDict ={
            'fullName':request.POST['fullName'],
            'email':request.POST['email'],
            'phone':request.POST['phone'],
            'total':(int(request.POST['amount']))
        }
        patientDict.update(feeDict)
       
        #for updating to database patientpaymentDetails (ppD)
        ppD=models.PatientPayementDetail()
        ppD.patientId=pk
        ppD.fullName=request.POST['fullName']
        ppD.email=request.POST['email']
        ppD.phone=request.POST['phone']
        ppD.receiver=receiverName
        ppD.receiverAccount=receiveraccount
        ppD.transactionId=transactionId
        ppD.paymentDate=date.today()
        ppD.paymentTime=datetime.now()
        ppD.amount=patient.medicinePrice
        ppD.total=(int(request.POST['amount']))
        ppD.save()
        print(feeDict)
        patient.status=True
        patient.save()
        return render(request,'hospital/patient_final_bill.html',context=patientDict)
    return render(request,'hospital/patient_generate_bill.html',context=patientDict)



@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_view_final_bill_view(request,pk):
    patient=models.LabTechRequestPayment.objects.get(id=pk)
    labTechId=models.User.objects.all().filter(id=patient.labTechId)
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    paymentDetails=models.PatientPayementDetails.objects.all().filter(patientId=patient.id).order_by('-id')[:1]
    patientDict=None
    if paymentDetails:
        patientDict ={
        'is_payed':True,
        'labTechId':labTechId,
        'patientId':patient.id,
        'fullName':paymentDetails[0].fullName,
        'email':paymentDetails[0].email,
        'address':paymentDetails[0].address,
        'state':paymentDetails[0].state,
        'bankName':paymentDetails[0].bankName,
        'accountNumber':paymentDetails[0].accountNumber,
        'receiverAccount':paymentDetails[0].receiverAccount,
        'email':paymentDetails[0].email,
        'email':paymentDetails[0].email,
        'amount':paymentDetails[0].amount,
        'total':paymentDetails[0].total,
        'patient':patient,
        }
        print(patientDict)
    else:
        patientDict={
            'is_payed':False,
            'patient':patient,
            'patientId':request.user.id,
        }
    return render(request,'hospital/labTech_check_patient_payment.html',context=patientDict)



#--------------for  patient bill (pdf) download and printing
import io
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return



def download_pdf_view(request,pk):
    paymentDetails=models.PatientPayementDetail.objects.all().filter(patientId=pk).order_by('-id')[:1]
    dict={
        'fullName':paymentDetails[0].fullName,
        'phone':paymentDetails[0].phone,
        'receiver':paymentDetails[0].receiver,
        'receiverAccount':paymentDetails[0].receiverAccount,
        'paymentTime':paymentDetails[0].paymentTime,
        'transactionId':paymentDetails[0].transactionId,
        'amount':paymentDetails[0].amount,

    }
    return render_to_pdf('hospital/download_bill.html',dict)



@login_required(login_url='labTechlogin')
@user_passes_test(is_lab_tech)
def labTech_view_labOrder_view(request):
    labtech=models.LabTech.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    laboratorys=models.Laboratory.objects.all().filter(status=True,labTechName=request.user.first_name)
    return render(request,'hospital/labTech_view_labOrder.html',{'laboratorys':laboratorys,'labtech':labtech})



@login_required(login_url='labTechlogin')
@user_passes_test(is_lab_tech)
def labTech_labOrder_view(request):
    labtech=models.LabTech.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    return render(request,'hospital/labTech_laboratory.html',{'labtech':labtech})


@login_required(login_url='pharmacistlogin')
@user_passes_test(is_pharmacist)
def pharmacist_dashboard_view(request):
    medicinecount=models.Medicine.objects.all().filter(status=True).count()    
    medicines=models.Medicine.objects.all().filter(status=True).order_by('-id')
    patientPayementSuccesscount=models.PharmacistRequestPayment.objects.all().filter(status=True,pharmacistId=request.user.id).count()
    prescriptionordercount=models.Prescription.objects.all().filter(status=True,pharmacistId=request.user.id).count()
    notificationcount=int(patientPayementSuccesscount + prescriptionordercount)
    mydict={
    'medicinecount':medicinecount,
    'medicines' :medicines,
    'pharmacist':models.Pharmacist.objects.get(user_id=request.user.id), #for profile picture of Pharmacist in sidebar
    'notificationcount':notificationcount,
    }
   
    return render(request,'hospital/pharmacist_dashboard.html',context=mydict)



@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_dashboard_view(request):
    #for three cards
    patientcount=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id).count()
    appointmentcount=models.Appointment.objects.all().filter(doctorId=request.user.id).count()    
    pendingappointmentcount=models.Appointment.objects.all().filter(status=False,doctorId=request.user.id).count()
    patientlabresult=models.PatientLabResult.objects.all().filter(doctorName=request.user.first_name)
    patientlabresultcount=models.PatientLabResult.objects.all().filter(doctorName=request.user.first_name).count()
    notificationcount=int(pendingappointmentcount + patientlabresultcount)
    #for  table in doctor dashboard
    appointments=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id).order_by('-id')
    patientid=[]
    for a in appointments:
        patientid.append(a.patientId)
    patients=models.Patient.objects.all().filter(status=True,user_id__in=patientid).order_by('-id')
    appointments=zip(appointments,patients)
    mydict={
    'patientcount':patientcount,
    'appointmentcount':appointmentcount,
    'appointments':appointments,
    'doctor':models.Doctor.objects.get(user_id=request.user.id), #for profile picture of doctor in sidebar
    'appointmentcount':appointmentcount,
    'notificationcount':notificationcount,
    'patientlabresult':patientlabresult
    }
    return render(request,'hospital/doctor_dashboard.html',context=mydict)



@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_patient_view(request):
    mydict={
    'doctor':models.Doctor.objects.get(user_id=request.user.id), #for profile picture of doctor in sidebar
    }
    return render(request,'hospital/doctor_patient.html',context=mydict)



@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_view_patient_view(request):
    appointments=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id).order_by('-id')
    patientid=[]
    for a in appointments:
        patientid.append(a.patientId)
    patients=models.Patient.objects.all().filter(status=True,user_id__in=patientid).order_by('-id')
    appointments=zip(appointments,patients)
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    return render(request,'hospital/doctor_view_patient.html',{'appointments':appointments,'patients':patients,'doctor':doctor})


@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_appointment_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    return render(request,'hospital/doctor_appointment.html',{'doctor':doctor})



@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_view_appointment_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    appointments=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id)
    patientid=[]
    for a in appointments:
        patientid.append(a.patientId)
    patients=models.Patient.objects.all().filter(status=True,user_id__in=patientid)
    appointments=zip(appointments,patients)
    totalappointement=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id).count()
    return render(request,'hospital/doctor_view_appointment.html',{'appointments':appointments,'doctor':doctor,'totalappointement':totalappointement})

@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_delete_appointment_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    appointments=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id)
    patientid=[]
    for a in appointments:
        patientid.append(a.patientId)
    patients=models.Patient.objects.all().filter(status=True,user_id__in=patientid)
    appointments=zip(appointments,patients)
    return render(request,'hospital/doctor_delete_appointment.html',{'appointments':appointments,'doctor':doctor})


@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def delete_appointment_view(request,pk):
    appointment=models.Appointment.objects.get(id=pk)
    appointment.delete()
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    appointments=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id)
    patientid=[]
    for a in appointments:
        patientid.append(a.patientId)
    patients=models.Patient.objects.all().filter(status=True,user_id__in=patientid)
    appointments=zip(appointments,patients)
    return render(request,'hospital/doctor_delete_appointment.html',{'appointments':appointments,'doctor':doctor})


@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_patient_diagnosis(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    diagnosisForm=forms.PatientDiagnosisForm()
    message=None
    mydict={'doctor':doctor,'diagnosisForm':diagnosisForm,'message':message,}
    if request.method=='POST':
        diagnosisForm=forms.PatientDiagnosisForm(request.POST)
        if diagnosisForm.is_valid():
            print(request.POST.get('patientId'))
            if  models.DoctorRecommondation.objects.all().filter(patent_Id=request.POST.get('patientId')) and models.Appointment.objects.all().filter(status=True,patientId=request.POST.get('patientId'),doctorId=request.user.id):
                symptoms=models.DoctorRecommondation.objects.all().filter(patent_Id=request.POST.get('patientId'))
                return render(request,'hospital/doctor_patient_diagnosis_view.html',{'symptoms':symptoms,'doctor':doctor})
            else:
                return render(request,'hospital/doctor_patient_diagnosis_forbiden.html')
    return render(request,'hospital/doctor_patient_diagnosis.html',context=mydict)


@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_patient_diagnosis_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    symptoms=models.DoctorRecommondation.objects.all().filter(patent_Id=request.POST.get('patientId'))
    return render(request,'hospital/doctor_patient_diagnosis_view.html',{'symptoms':symptoms,'doctor':doctor})


@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_patient_labResult_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    patientLabResults=models.PatientLabResult.objects.all().filter(doctorName=request.user.first_name)
    return render(request,'hospital/doctor_view_patient_labResult.html',{'patientLabResults':patientLabResults,'doctor':doctor})


@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_schedule_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of  in sidebar
    schedule=models.ScheduleAppointment.objects.all().filter(doctorName=request.user.first_name)
    return render(request,'hospital/doctor_view_schedule.html',{'schedule':schedule,'doctor':doctor})



@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_dashboard_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id)
    totalbookedappointmentcount=models.Appointment.objects.all().filter(patientId=request.user.id).count()
    approvedappointmentcount=models.Appointment.objects.all().filter(status=True,patientId=request.user.id).count()
    labPaymentRequest=models.LabTechRequestPayment.objects.all().filter(status=False,patientName=request.user.first_name).count()
    medicinePaymentRequest=models.PharmacistRequestPayment.objects.all().filter(status=False,patientName=request.user.first_name).count()
    announcementFromDoctorcount=models.Announcement.objects.all().filter(patientId=request.user.id).count()
    notificationcount=int(labPaymentRequest + medicinePaymentRequest + announcementFromDoctorcount)
    appointments=models.Appointment.objects.all().filter(patientId=request.user.id).order_by('-id')
    mydict={
    'patient':patient,
    'appointments':appointments,
    'approvedappointmentcount':approvedappointmentcount,
    'admitDate':patient.admitDate,
    'labPaymentRequest':labPaymentRequest,
    'notificationcount':notificationcount,
    'totalbookedappointmentcount':totalbookedappointmentcount,
    }
    return render(request,'hospital/patient_dashboard.html',context=mydict)



@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_appointment_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    return render(request,'hospital/patient_appointment.html',{'patient':patient})



@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_book_appointment(request):
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar    
    appointementform=forms.PatientAppointment()
    message=None
    doctors=models.Doctor.objects.all().filter(status=True,department='Cardiologist').order_by('-id')
    mydict={'appointementform':appointementform,'message':message,'patient':patient,}
    if request.method=='POST':
            appointementform=forms.PatientAppointment(request.POST)
            if appointementform.is_valid():
                sympt=request.POST.get('symptoms')
                if 'heart' in sympt or 'chestpain'in sympt or 'breath'in sympt  :
                    if  models.Doctor.objects.all().filter(status=True,department='Cardiologist').exists():
                        doctors=models.Doctor.objects.all().filter(status=True,department='Cardiologist').order_by('-id')
                        messages.info(request, " ")
                        appointement=appointementform.save(commit=False)
                        appointement.symptomId=models.Symptom.objects.all().count()+1
                        appointement.patientId=request.user.id #----user can choose any patient but only their info will be stored
                        appointement.patientName=request.user.first_name #----user can choose any patient but only their info will be stored
                        appointement.status=True
                        appointement.save()                       
                        return render(request,'hospital/patient_book_appointment_detail_view.html',{'appointementform':appointementform,'message':message,'doctors' :doctors,'patient':patient,})

                elif 'accident' in sympt or 'headache'in sympt or 'fever'in sympt:
                    if  models.Doctor.objects.all().filter(status=True,department='EmergencyDepartement').exists():
                        doctors=models.Doctor.objects.all().filter(status=True,department='EmergencyDepartement').order_by('-id')
                        messages.info(request, " ")
                        appointement=appointementform.save(commit=False)
                        appointement.symptomId= models.Symptom.objects.all().count()+1
                        appointement.patientId=request.user.id #----user can choose any patient but only their info will be stored
                        appointement.patientName=request.user.first_name #----user can choose any patient but only their info will be stored
                        appointement.status=True
                        appointement.save()
                        return render(request,'hospital/patient_book_appointment_detail_view.html',{'appointementform':appointementform,'message':message,'doctors' :doctors,'patient':patient})
                elif 'mentaldisorder' in sympt or 'depression'in sympt or 'anxiety'in sympt:
                    if  models.Doctor.objects.all().filter(status=True,department='Psychiatrist').exists():
                        doctors=models.Doctor.objects.all().filter(status=True,department='Psychiatrist').order_by('-id')
                        messages.info(request, " ")
                        appointement=appointementform.save(commit=False)
                        appointement.symptomId= models.Symptom.objects.all().count()+1
                        appointement.patientId=request.user.id #----user can choose any patient but only their info will be stored
                        appointement.patientName=request.user.first_name #----user can choose any patient but only their info will be stored
                        appointement.status=True
                        appointement.save()
                        return render(request,'hospital/patient_book_appointment_detail_view.html',{'appointementform':appointementform,'message':message,'doctors' :doctors,'patient':patient})
                elif 'skin' in sympt or 'skincancer'in sympt or 'hair'in sympt:
                    if  models.Doctor.objects.all().filter(status=True,department='Dermatologist').exists():
                        doctors=models.Doctor.objects.all().filter(status=True,department='Dermatologist').order_by('-id')
                        messages.info(request, " ")
                        appointement=appointementform.save(commit=False)
                        appointement.symptomId= models.Symptom.objects.all().count()+1
                        appointement.patientId=request.user.id #----user can choose any patient but only their info will be stored
                        appointement.patientName=request.user.first_name #----user can choose any patient but only their info will be stored
                        appointement.status=True
                        appointement.save()
                        return render(request,'hospital/patient_book_appointment_detail_view.html',{'appointementform':appointementform,'message':message,'doctors' :doctors,'patient':patient,})
                elif 'allergy' in sympt or 'asthma'in sympt or 'immunedisorder'in sympt:
                    if  models.Doctor.objects.all().filter(status=True,department='Allergist').exists():
                        doctors=models.Doctor.objects.all().filter(status=True,department='Allergist').order_by('-id')
                        messages.info(request, " ")
                        appointement=appointementform.save(commit=False)
                        appointement.symptomId= models.Symptom.objects.all().count()+1
                        appointement.patientId=request.user.id #----user can choose any patient but only their info will be stored
                        appointement.patientName=request.user.first_name #----user can choose any patient but only their info will be stored
                        appointement.status=True
                        appointement.save()
                        return render(request,'hospital/patient_book_appointment_detail_view.html',{'appointementform':appointementform,'message':message,'doctors' :doctors,'patient':patient,})
                elif 'infant' in sympt or 'children'in sympt or 'adolescent'in sympt:
                    if  models.Doctor.objects.all().filter(status=True,department='Pediatrician').exists():
                        doctors=models.Doctor.objects.all().filter(status=True,department='Pediatrician').order_by('-id')
                        messages.info(request, " ")
                        appointement=appointementform.save(commit=False)
                        appointement.symptomId= models.Symptom.objects.all().count()+1
                        appointement.patientId=request.user.id #----user can choose any patient but only their info will be stored
                        appointement.patientName=request.user.first_name #----user can choose any patient but only their info will be stored
                        appointement.status=True
                        appointement.save()
                        return render(request,'hospital/patient_book_appointment_detail_view.html',{'appointementform':appointementform,'message':message,'doctors' :doctors,'patient':patient})
                elif 'surgery' in sympt or 'obstetrics'in sympt or 'vomiting'in sympt:
                    if  models.Doctor.objects.all().filter(status=True,department='Anesthesiologist').exists():
                        doctors=models.Doctor.objects.all().filter(status=True,department='Anesthesiologist').order_by('-id')
                        messages.info(request, " ")
                        appointement=appointementform.save(commit=False)
                        appointement.symptomId= models.Symptom.objects.all().count()+1
                        appointement.patientId=request.user.id #----user can choose any patient but only their info will be stored
                        appointement.patientName=request.user.first_name #----user can choose any patient but only their info will be stored
                        appointement.status=True
                        appointement.save()
                        return render(request,'hospital/patient_book_appointment_detail_view.html',{'appointementform':appointementform,'message':message,'doctors' :doctors,'patient':patient})               
 
                elif 'cancer' in sympt or 'therapy'in sympt or 'cancersurgeon'in sympt:
                    if  models.Doctor.objects.all().filter(status=True,department='Oncologist').exists():
                        doctors=models.Doctor.objects.all().filter(status=True,department='Oncologist').order_by('-id')
                        messages.info(request, " ")
                        appointement=appointementform.save(commit=False)
                        appointement.symptomId= models.Symptom.objects.all().count()+1
                        appointement.patientId=request.user.id #----user can choose any patient but only their info will be stored
                        appointement.patientName=request.user.first_name #----user can choose any patient but only their info will be stored
                        appointement.status=True
                        appointement.save()
                        return render(request,'hospital/patient_book_appointment_detail_view.html',{'appointementform':appointementform,'message':message,'doctors' :doctor,'patient':patients})               

                elif 'bone' in sympt or 'muscle'in sympt or 'musculoskeletal'in sympt:
                    if  models.Doctor.objects.all().filter(status=True,department='Orthopedist').exists():
                        doctors=models.Doctor.objects.all().filter(status=True,department='Orthopedist').order_by('-id')
                        messages.info(request, " ")
                        appointement=appointementform.save(commit=False)
                        appointement.symptomId= models.Symptom.objects.all().count()+1
                        appointement.patientId=request.user.id #----user can choose any patient but only their info will be stored
                        appointement.patientName=request.user.first_name #----user can choose any patient but only their info will be stored
                        appointement.status=True
                        appointement.save()
                        return render(request,'hospital/patient_book_appointment_detail_view.html',{'appointementform':appointementform,'message':message,'doctors' :doctors,'patient':patient})               
 
                elif 'urinate' in sympt or 'swelling'in sympt or 'fatigue'in sympt or 'urine'in sympt or 'urination'in sympt:
                    if  models.Doctor.objects.all().filter(status=True,department='Nephrologist').exists():
                        doctors=models.Doctor.objects.all().filter(status=True,department='Nephrologist').order_by('-id')
                        messages.info(request, " ")
                        appointement=appointementform.save(commit=False)
                        appointement.symptomId= models.Symptom.objects.all().count()+1
                        appointement.patientId=request.user.id #----user can choose any patient but only their info will be stored
                        appointement.patientName=request.user.first_name #----user can choose any patient but only their info will be stored
                        appointement.status=True
                        appointement.save()
                        return render(request,'hospital/patient_book_appointment_detail_view.html',{'appointementform':appointementform,'message':message,'doctors' :doctors,'patient':patient})               
 
                else:
                    messages.info(request, ",")
                    appointement=appointementform.save(commit=False)
                    appointement.symptomId=models.Symptom.objects.all().count()+1
                    appointement.patientId=request.user.id #----user can choose any patient but only their info will be stored
                    appointement.patientName=request.user.first_name #----user can choose any patient but only their info will be stored
                    appointement.status=True
                    appointement.save()
                    return render(request,'hospital/patient_book_appointment_detail_view.html',{'appointementform':appointementform,'message':message,'patient':patient})

    return render(request,'hospital/patient_book_appointment_veiw.html',context=mydict)



@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_book_apointement_details_views(request,pk):
    Message=None
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture   in sidebar
    doctor=models.Doctor.objects.get(id=pk)
    user=models.User.objects.get(id=doctor.user_id)
    userForm=forms.DoctorUserForm(instance=user)
    doctorForm=forms.DoctorForm(instance=doctor)
    checkappointements=models.Appointment.objects.all().filter(doctorUserName=user.username)
    appointementSchedule=models.ScheduleAppointment.objects.all().filter(doctorId=doctor.user.id)    
    appointementForm=forms.PatientAppointmentForm()
    mydict={'userForm':userForm,'doctorForm':doctorForm,'appointementForm':appointementForm,'patient':patient,'appointementSchedule':appointementSchedule,'checkappointements':checkappointements,'Message':Message}
    if request.method=='POST':
        appointementForm=forms.PatientAppointmentForm(request.POST)
        if appointementForm.is_valid():
            appointment=appointementForm.save(commit=False)
            appointment.patientId=request.user.id #----user can choose any patient but only their info will be stored '11:42:35,173'
            appointment.doctorName=models.User.objects.get(id=doctor.user_id).first_name
            appointment.patientName=request.user.first_name #----user can choose any patient but only their info will be stored
            appointment.doctorId=models.User.objects.get(id=doctor.user_id).id#----user can choose any patient but only their info will be stored
            appointment.doctorUserName=models.User.objects.get(id=doctor.user_id).username#----user can choose any patient but only their info will be stored
            appointment.status=False
            appointment.appointmentTime= request.POST['appointement']
            
            if checkappointements and \
            models.Appointment.objects.filter(appointmentDate=appointment.appointmentDate, appointmentTime=appointment.appointmentTime).exists():
                messages.info(request, "The Appointment Time Was Already Taken.")
            else:
                appointment.save()
                return redirect('patient-view-appointment')       

    return render(request,'hospital/patient_book_appointment_detail.html',context=mydict)


   
@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_view_appointment_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    appointments=models.Appointment.objects.all().filter(patientId=request.user.id)
    totalbookedappointmentcount=models.Appointment.objects.all().filter(patientId=request.user.id).count()
    return render(request,'hospital/patient_view_appointment.html',{'appointments':appointments,'totalbookedappointmentcount':totalbookedappointmentcount,'patient':patient})


#------------------telemedicine start---------------------

def patient_telemedicine_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id)

    return render(request, 'base/patient_telemedicine.html',{'patient':patient})

def doctor_telemedicine_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id)

    return render(request, 'base/doctor_telemedicine.html',{'doctor':doctor})

def patient_room_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id)

    return render(request, 'base/patient_room.html',{'patient':patient})

def doctor_room_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id)

    return render(request, 'base/doctor_room.html',{'doctor':doctor})


def getToken(request):
    appId = "0f120f3e511a4e64863983e7ff69b895"
    appCertificate = "9e31fc27a9c0497c971e4a336ee5c2a8"
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600
    currentTimeStamp = int(time.time())
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)

    return JsonResponse({'token': token, 'uid': uid}, safe=False)


@csrf_exempt
def createMember(request):
    data = json.loads(request.body)
    member, created = RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )

    return JsonResponse({'name':data['name']}, safe=False)


def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(
        uid=uid,
        room_name=room_name,
    )
    name = member.name
    return JsonResponse({'name':member.name}, safe=False)

@csrf_exempt
def deleteMember(request):
    data = json.loads(request.body)
    member = RoomMember.objects.get(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )
    member.delete()
    return JsonResponse('Member deleted', safe=False)

#--------------telemedicine end--------------

#-----------------payment start-----------------

def patientLaboratoryTestPayementProcessing(request,pk):
        patient=models.LabTechRequestPayment.objects.get(id=pk)
        random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=9))
        transactionId = "FT248056HqR" + random_chars

        dictionary = {
            'amount':patient.testPrice,
            'patient':patient,
            'tx_ref':transactionId,
            'patient':models.Patient.objects.get(user_id=request.user.id)

            }

        patient.status=True
        patient.save()
        return render(request, 'hospital/patient_laboratory_test_payment_processing.html',context=dictionary)

def successMsgLaboratoryTestPayement(request):
    patient=models.Patient.objects.get(user_id=request.user.id)

    return render(request, 'hospital/patient_laboratory_test_payement_success.html',{'patient':patient})


def patientMedicinePayementProcessing(request,pk):
    patient=models.PharmacistRequestPayment.objects.get(id=pk)

    random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=9))
    transactionId = "FT248056HqR" + random_chars
    dictionary = {
        'amount':patient.medicinePrice,
        'patient':patient,
        'tx_ref':transactionId,
        'patient':models.Patient.objects.get(user_id=request.user.id)

        }

    patient.status=True
    patient.save()
    return render(request, 'hospital/patient_medicine_payment_processing.html',context=dictionary)

def successMsgMedicinePayement(request):
    patient=models.Patient.objects.get(user_id=request.user.id)

    return render(request, 'hospital/patient_medicine_payement_success.html',{'patient':patient})


#-------------------------payment end--------------

# recommendations/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Patient, Doctor, Symptom,DoctorRecommondation
from .forms import DoctorRecommondationForm
from .ml_model import recommend_doctor


def patient_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id)
    if request.method == 'POST':
        form = DoctorRecommondationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            symptoms = form.cleaned_data['symptoms']
            patient = DoctorRecommondation(name=name)
            patient.save()  # Save the patient to generate an ID
            
            for symptom in symptoms:
                patient.symptoms.add(symptom)

            symptom = [symptom.name for symptom in patient.symptoms.all()]
            symptm = ",".join([symptom.name for symptom in patient.symptoms.all()])

            print(f"Selected symptoms: {symptom}")  # Debugging line
            
            top_specializations = recommend_doctor([symptom.name for symptom in symptoms])
            recommended_doctors = []
            for department in top_specializations:
                doctors_with_specialization = Doctor.objects.filter(department__iexact=department)
                recommended_doctors.extend(doctors_with_specialization.order_by('-expriance')[:2])

                print(f"Doctors with specialization {department}: {doctors_with_specialization}")

            # Save recommended doctors to the patient's recommended_doctor field
            patient.recommended_doctor.set(recommended_doctors)
            print(f"Recommended doctor: {recommended_doctors}")  # Debugging line

            patient.selected_symptoms=symptm 
            patient.symptmId=models.DoctorRecommondation.objects.all().count()+1
            patient.patent_Id=request.user.id
            patient.save()  # Now save the patient with the recommended doctor
            return redirect('recommendation_result', patient_id=patient.id)
    else:
        form = DoctorRecommondationForm()
    return render(request, 'hospital/patient_form.html', {'form': form,'patient':patient})

def recommendation_result(request, patient_id):
    patient = get_object_or_404(DoctorRecommondation, id=patient_id)
    recommended_doctors = patient.recommended_doctor.all().order_by('-expriance')
    return render(request, 'hospital/recommendation_result.html', {
        'patient': patient,
        'recommended_doctors': recommended_doctors
    })



#-----------------------contact start--------------


def contactus_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            return render(request, 'hospital/contactussuccess.html')
    return render(request, 'hospital/contactus.html', {'form':sub})


#-------------------------contact end--------------
