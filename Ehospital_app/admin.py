from django.contrib import admin
from .models import Doctor,Patient,Appointment,Hospital,Pharmacist,LabTech,Medicine,Prescription,Laboratory,LabTechRequestPayment,RoomMember,PatientPayementDetail,PatientLabResult,PharmacistRequestPayment,PatientMedicineInstruction,ScheduleAppointment,Symptom,Announcement,DoctorRecommondation

# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctor, DoctorAdmin)

class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)

class AppointmentDoctor(admin.ModelAdmin):
    pass
admin.site.register(Appointment, AppointmentDoctor)

class HospitalAdmin(admin.ModelAdmin):
    pass
admin.site.register(Hospital, HospitalAdmin)


class Pharmacistadmin(admin.ModelAdmin):
    pass
admin.site.register(Pharmacist, Pharmacistadmin)

class LabTechAdmin(admin.ModelAdmin):
    pass
admin.site.register(LabTech, LabTechAdmin)

class MedicinePharmacist(admin.ModelAdmin):
    pass
admin.site.register(Medicine, MedicinePharmacist)

class PrescriptionDoctor(admin.ModelAdmin):
    pass
admin.site.register(Prescription, PrescriptionDoctor)

class LabOrderDoctor(admin.ModelAdmin):
    pass
admin.site.register(Laboratory, LabOrderDoctor)


class Lab_TechRequestPayment(admin.ModelAdmin):
    pass
admin.site.register(LabTechRequestPayment, Lab_TechRequestPayment)

class DoctorPatientChat(admin.ModelAdmin):
    pass
admin.site.register(RoomMember, DoctorPatientChat)

class PatientPayement(admin.ModelAdmin):
    pass
admin.site.register(PatientPayementDetail, PatientPayement)

class PatientLabResultReport(admin.ModelAdmin):
    pass
admin.site.register(PatientLabResult, PatientLabResultReport)

class PatientPharmacistRequestPayment(admin.ModelAdmin):
    pass
admin.site.register(PharmacistRequestPayment, PatientPharmacistRequestPayment)

class PatientPharmacistMedicineInstruction(admin.ModelAdmin):
    pass 
admin.site.register(PatientMedicineInstruction, PatientPharmacistMedicineInstruction)

class AdminScheduleAppointment(admin.ModelAdmin):
    pass
admin.site.register(ScheduleAppointment, AdminScheduleAppointment)

class PostAnnouncement(admin.ModelAdmin):
    pass
admin.site.register(Announcement, PostAnnouncement)

class DoctorRecommondSystem(admin.ModelAdmin):
    pass
admin.site.register(DoctorRecommondation, DoctorRecommondSystem)

class PatientSymptom(admin.ModelAdmin):
    pass
admin.site.register(Symptom, PatientSymptom)
