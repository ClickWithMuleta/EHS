from django import forms
from django.contrib.auth.models import User
from . import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.password_validation import validate_password
from django.core.validators import RegexValidator
from datetime import datetime, time
import random
from .models import Appointment
from .models import Patient,Symptom,DoctorRecommondation

class DoctorRecommondationForm(forms.ModelForm):
    symptoms = forms.ModelMultipleChoiceField(queryset=Symptom.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = DoctorRecommondation
        fields = ['name', 'symptoms']

# for register new admin 
class RegisterAdminForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise forms.ValidationError("First name cannot be empty.")
        if len(first_name) <= 3:
            raise forms.ValidationError("First name must be longer than 3 characters.")
        if not first_name.isalpha():
            raise forms.ValidationError("First name must contain only letters.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name:
            raise forms.ValidationError("Last name cannot be empty.")
        if len(last_name) <= 3:
            raise forms.ValidationError("Last name must be longer than 3 characters.")
        if not last_name.isalpha():
            raise forms.ValidationError("Last name must contain only letters.")
        return last_name

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError("username cannot be empty.")
        if len(username) <= 5:
            raise forms.ValidationError("username must be longer than 5 characters.")
        if not username.isalnum():
            raise forms.ValidationError("Username must contain only letters and numbers.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        try:
            validate_password(password)
        except ValidationError as e:
            raise forms.ValidationError(e.messages)
        return password

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']



# for doctor related form

class DoctorUserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise forms.ValidationError("First name cannot be empty.")
        if len(first_name) < 3:
            raise forms.ValidationError("First name must be longer than 3 characters.")
        if not first_name.isalpha():
            raise forms.ValidationError("First name must contain only letters.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name:
            raise forms.ValidationError("Last name cannot be empty.")
        if len(last_name) <= 3:
            raise forms.ValidationError("Last name must be longer than 3 characters.")
        if not last_name.isalpha():
            raise forms.ValidationError("Last name must contain only letters.")
        return last_name

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError("username cannot be empty.")
        if len(username) <= 5:
            raise forms.ValidationError("username must be longer than 5 characters.")
        if not username.isalnum():
            raise forms.ValidationError("Username must contain only letters and numbers.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        try:
            validate_password(password)
        except ValidationError as e:
            raise forms.ValidationError(e.messages)
        return password

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


class DoctorForm(forms.ModelForm):

    hospital_Id=forms.ModelChoiceField(queryset=models.Hospital.objects.all(),empty_label="Choose Hospital to Assign", to_field_name="hospitalName")

    def clean_address(self):
        address = self.cleaned_data.get('address')
        if not address:
            raise forms.ValidationError("Address cannot be empty.")
        return address

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')

        # Validate Ethiopian phone number format
        if not re.match(r'^(07|09|\+2519)\d{8}$', mobile):
            raise forms.ValidationError("Enter a valid Ethiopian phone number.")
        return mobile

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email cannot be empty.")
        return email

    class Meta:
        model=models.Doctor
        fields=['address','mobile','email','department','expriance','certification','status','profile_pic']


# for patient related form

class PatientUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise forms.ValidationError("First name cannot be empty.")
        if len(first_name) <= 3:
            raise forms.ValidationError("First name must be longer than 3 characters.")
        if not first_name.isalpha():
            raise forms.ValidationError("First name must contain only letters.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name:
            raise forms.ValidationError("Last name cannot be empty.")
        if len(last_name) <= 3:
            raise forms.ValidationError("Last name must be longer than 3 characters.")
        if not last_name.isalpha():
            raise forms.ValidationError("Last name must contain only letters.")
        return last_name

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError("username cannot be empty.")
        if len(username) <= 5:
            raise forms.ValidationError("username must be longer than 5 characters.")
        if not username.isalnum():
            raise forms.ValidationError("Username must contain only letters and numbers.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        try:
            validate_password(password)
        except ValidationError as e:
            raise forms.ValidationError(e.messages)
        return password

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']

class PatientForm(forms.ModelForm):

    def clean_address(self):
        address = self.cleaned_data.get('address')
        if not address:
            raise forms.ValidationError("Address cannot be empty.")
        return address

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')

        # Validate Ethiopian phone number format
        if not re.match(r'^(07|09|\+2519)\d{8}$', mobile):
            raise forms.ValidationError("Enter a valid Ethiopian phone number.")
        return mobile

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email cannot be empty.")
        return email

    class Meta:
        model = models.Patient
        fields = ['address', 'mobile', 'email', 'status', 'profile_pic']




class PatientAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appointmentDate', 'status']
        widgets = {
            'appointmentDate': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(PatientAppointmentForm, self).__init__(*args, **kwargs)
        
        # Set the initial value to today
        self.fields['appointmentDate'].initial = timezone.now().date()
        
        # Set the minimum date to today
        self.fields['appointmentDate'].widget.attrs['min'] = datetime.now().strftime('%Y-%m-%d')



# for Patient Diagnosis Form

class PatientDiagnosisForm(forms.ModelForm):
    patientId=forms.ModelChoiceField(queryset=models.Patient.objects.all().filter(status=True),empty_label="Select Your Patient ", to_field_name="user_id")
    class Meta:
        model=models.Symptom
        fields=['status']


# for Announcement Form

class AnnouncementForm(forms.ModelForm):
    patientId=forms.ModelChoiceField(queryset=models.Patient.objects.all().filter(status=True),empty_label="Patient ", to_field_name="user_id")
    class Meta:
        model=models.Announcement
        fields=['message']



# for Hospital related form

class HospitalForm(forms.ModelForm):

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')

        # Validate Ethiopian phone number format
        if not re.match(r'^(07|09|\+2519)\d{8}$', mobile):
            raise forms.ValidationError("Enter a valid Ethiopian phone number.")
        return mobile

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email cannot be empty.")
        return email
    class Meta:
        model=models.Hospital
        fields=['hospitalName','address','email','mobile','description' ,'hospital_pic']
        widgets = {
        'email': forms.EmailInput()
        }



# for pharmacist related form

class PharmacistUserForm(forms.ModelForm): 

    password = forms.CharField(widget=forms.PasswordInput())

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise forms.ValidationError("First name cannot be empty.")
        if len(first_name) <= 3:
            raise forms.ValidationError("First name must be longer than 3 characters.")
        if not first_name.isalpha():
            raise forms.ValidationError("First name must contain only letters.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name:
            raise forms.ValidationError("Last name cannot be empty.")
        if len(last_name) <= 3:
            raise forms.ValidationError("Last name must be longer than 3 characters.")
        if not last_name.isalpha():
            raise forms.ValidationError("Last name must contain only letters.")
        return last_name

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError("username cannot be empty.")
        if len(username) <= 5:
            raise forms.ValidationError("username must be longer than 5 characters.")
        if not username.isalnum():
            raise forms.ValidationError("Username must contain only letters and numbers.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        try:
            validate_password(password)
        except ValidationError as e:
            raise forms.ValidationError(e.messages)
        return password

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


class PharmacistForm(forms.ModelForm):
    hospital_Id=forms.ModelChoiceField(queryset=models.Hospital.objects.all(),empty_label="Choose Hospital to Assign", to_field_name="hospitalName")

    def clean_address(self):
        address = self.cleaned_data.get('address')
        if not address:
            raise forms.ValidationError("Address cannot be empty.")
        return address

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')

        # Validate Ethiopian phone number format
        if not re.match(r'^(07|09|\+2519)\d{8}$', mobile):
            raise forms.ValidationError("Enter a valid Ethiopian phone number.")
        return mobile

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email cannot be empty.")
        return email

    class Meta:
        model = models.Pharmacist
        fields = ['address', 'mobile', 'email', 'status', 'profile_pic']




# for Lab_Tech related form

class Lab_TechUserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise forms.ValidationError("First name cannot be empty.")
        if len(first_name) <= 3:
            raise forms.ValidationError("First name must be longer than 3 characters.")
        if not first_name.isalpha():
            raise forms.ValidationError("First name must contain only letters.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name:
            raise forms.ValidationError("Last name cannot be empty.")
        if len(last_name) <= 3:
            raise forms.ValidationError("Last name must be longer than 3 characters.")
        if not last_name.isalpha():
            raise forms.ValidationError("Last name must contain only letters.")
        return last_name

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError("username cannot be empty.")
        if len(username) <= 5:
            raise forms.ValidationError("username must be longer than 5 characters.")
        if not username.isalnum():
            raise forms.ValidationError("Username must contain only letters and numbers.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        try:
            validate_password(password)
        except ValidationError as e:
            raise forms.ValidationError(e.messages)
        return password

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


class Lab_TechForm(forms.ModelForm):

    hospital_Id=forms.ModelChoiceField(queryset=models.Hospital.objects.all(),empty_label="Choose Hospital to Assign", to_field_name="hospitalName")

    def clean_address(self):
        address = self.cleaned_data.get('address')
        if not address:
            raise forms.ValidationError("Address cannot be empty.")
        return address

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')

        # Validate Ethiopian phone number format
        if not re.match(r'^(07|09|\+2519)\d{8}$', mobile):
            raise forms.ValidationError("Enter a valid Ethiopian phone number.")
        return mobile

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email cannot be empty.")
        return email

    class Meta:
        model = models.LabTech
        fields = ['address', 'mobile', 'email', 'status', 'profile_pic']


# for medicine related form

class MedicineForm(forms.ModelForm):
    class Meta:
        model = models.Medicine
        fields = ['medicineName', 'quantity', 'price', 'Date','status']
        widgets = {
            'Date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }
            )
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if not isinstance(quantity, (int, float)) or quantity <= 0:
            raise forms.ValidationError("Quantity must be a positive number.")
        return quantity

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if not isinstance(price, (int, float)) or price <= 0:
            raise forms.ValidationError("Price must be a positive number.")
        return price




 # for Prescription related form

class PrescriptionForm(forms.ModelForm):
    pharmacistId=forms.ModelChoiceField(queryset=models.Pharmacist.objects.all().filter(status=True),empty_label="Pharmacist Name ", to_field_name="user_id")
    
    def clean_doctorName(self):
        doctorName = self.cleaned_data.get('doctorName')
        if not doctorName:
            raise forms.ValidationError("Your  name cannot be empty.")
        if len(doctorName) <= 3:
            raise forms.ValidationError(" Name must be longer than 3 characters.")
        if not doctorName.isalpha():
            raise forms.ValidationError(" Name must contain only letters.")
        return doctorName

    def clean_patientName(self):
        patientName = self.cleaned_data.get('patientName')
        if not patientName:
            raise forms.ValidationError("Patient name cannot be empty.")
        if len(patientName) <= 3:
            raise forms.ValidationError("Patient name must be longer than 3 characters.")
        if not patientName.isalpha():
            raise forms.ValidationError("Patient name must contain only letters.")
        return patientName

    def clean_medicine(self):
        medicine = self.cleaned_data.get('medicine')
        if not medicine:
            raise forms.ValidationError("medicine cannot be empty.")
        return medicine

    def clean_dosage(self):
        dosage = self.cleaned_data.get('dosage')
        if not dosage:
            raise forms.ValidationError("dosage cannot be empty.")
        return dosage
    def clean_numberOfDays(self):
        numberOfDays = self.cleaned_data.get('numberOfDays')
        if not numberOfDays:
            raise forms.ValidationError("Number of days cannot be empty.")
        try:
            numberOfDays = int(numberOfDays)
            if numberOfDays <= 0:
                raise forms.ValidationError("Number of days must be a positive number.")
        except ValueError:
            raise forms.ValidationError("Number of days must be a valid integer.")
        return numberOfDays
    
    class Meta:
        model=models.Prescription
        fields=['doctorName','patientName','medicine','dosage','numberOfDays','status']



  #for laboratory related form

class LaboratoryForm(forms.ModelForm):
    labTechId=forms.ModelChoiceField(queryset=models.LabTech.objects.all().filter(status=True),empty_label="Lab Technician Name ", to_field_name="user_id")
    
    def clean_doctorName(self):
        doctorName = self.cleaned_data.get('doctorName')
        if not doctorName:
            raise forms.ValidationError(" Name cannot be empty.")
        if len(doctorName) <= 3:
            raise forms.ValidationError(" Name must be longer than 3 characters.")
        if not doctorName.isalpha():
            raise forms.ValidationError(" Name must contain only letters.")
        return doctorName
    def clean_patientName(self):
        patientName = self.cleaned_data.get('patientName')
        if not patientName:
            raise forms.ValidationError(" Name cannot be empty.")
        if len(patientName) <= 3:
            raise forms.ValidationError(" Name must be longer than 3 characters.")
        if not patientName.isalpha():
            raise forms.ValidationError(" Name must contain only letters.")
        return patientName

    class Meta:
        model=models.Laboratory
        fields=['doctorName','patientName','orderDate','status']
        widgets = {
            'orderDate': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }
            )
        }




# for labrequsetpayment related form

class LabTechRequestPaymentForm(forms.ModelForm):

    class Meta:
        model=models.LabTechRequestPayment
        fields=['doctorName','patientName','sampleType','orderDate','description','testPrice','status']



# for medicinepayment related form

class PharmacistRequestPaymentForm(forms.ModelForm):

    class Meta:
        model=models.PharmacistRequestPayment
        fields=['doctorName','patientName','medicine','dosage','numberOfDays','description','medicinePrice','status']



# for labresult related form

class PatientLabResultForm(forms.ModelForm):

    class Meta:
        model=models.PatientLabResult
        fields=['doctorName','patientName','sampleType','orderDate','labResult']



# for medicine instruction related form

class PharmacistGiveMedicineInstructionForm(forms.ModelForm):

    class Meta:
        model=models.PatientMedicineInstruction
        fields=['patientName','doctorName','medicine','dosage','numberOfDays','instruction','status']



# for contact us page form

class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
