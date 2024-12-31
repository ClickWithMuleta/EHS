from django.contrib import admin
from django.urls import path
from Ehospital_app import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include


urlpatterns =[

    path('',views.index,name='index'),
    path('doctor-detail-view/<int:pk>',views.doctor_detail_view,name='doctor-detail-view'),
    path('hospital-detail-view/<int:pk>',views.hospital_detail_view,name='hospital-detail-view'),
    path('login', views.login_view ,name='login'),
    path('logout_view', views.logoutView, name='logout_view'),
    path('about', views.aboutus_view),
    path('services', views.services_view),
    path('contactus',views.contactus_view),
    path('departement',views.departement_view),
    path('cardiologist-departement', views.Cardiologist_departement_view),
    path('anesthsiologst-departement', views.Anesthesiologists_departement_view),
    path('dermatologist-departement', views.Dermatologists_departement_view),
    path('emergency-departement', views.Emergency_departement_view),
    path('allergy-departement', views.Allergists_departement_view),
    path('psychatrist-departement', views.Psychiatrist_departement_view),
    path('pediatrician-departement', views.Pediatrician_departement_view),
    path('orthopedist-departement', views.Orthopedist_departement_view),
    path('oncologist-departement', views.Oncologist_departement_view),
    path('nephrologist-departement', views.Nephrologist_departement_view),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),

#------------------Telemedicine Solution------------------------

    path('patient-room/', views.patient_room_view),
    path('doctor-room/', views.doctor_room_view),
    path('get_token/', views.getToken),
    path('create_member/', views.createMember),
    path('get_member/', views.getMember),
    path('delete_member/', views.deleteMember),
    path('doctor-vedio-calling', views.doctor_telemedicine_view),
    path('patient-vedio-calling', views.patient_telemedicine_view),

#-----------------Payment Processing----------------

    path('patient-laboratory-test-payment-processing/<int:pk>', views.patientLaboratoryTestPayementProcessing, name="patient-laboratory-test-payment-processing"),
    path('patient-laboratory-test-payment-success', views.successMsgLaboratoryTestPayement, name="patient-laboratory-test-payment-success"),
    path('patient-medicine-payment-processing/<int:pk>', views.patientMedicinePayementProcessing, name="patient-medicine-payment-processing"),
    path('patient-medicine-payment-success', views.successMsgMedicinePayement, name="patient-medicine-payment-success"),


    path('patient/', views.patient_view, name='patient_form'),
    path('recommonded-doctors/<int:patient_id>/', views.recommendation_result, name='recommendation_result'),

]

#-------------FOR ADMIN RELATED URLS---------------

urlpatterns += [

    path('admin/', admin.site.urls),
    path('register-admin', views.admin_register_new_admin_view),
    path('admin-notification', views.admin_notification_view,name='admin-notification'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    path('admin-doctor', views.admin_doctor_view,name='admin-doctor'),
    path('admin-view-doctor', views.admin_view_doctor_view,name='admin-view-doctor'),
    path('delete-doctor-from-hospital/<int:pk>', views.delete_doctor_from_hospital_view,name='delete-doctor-from-hospital'),
    path('update-doctor/<int:pk>', views.update_doctor_view,name='update-doctor'),
    path('admin-add-doctor', views.admin_add_doctor_view,name='admin-add-doctor'),
    path('admin-view-doctor-certification-and-specialization',views.admin_view_doctor_specialisation_view,name='admin-view-doctor-certification-and-specialization'),
    path('admin-view-doctor-certification/<int:pk>', views.admin_view_doctor_certification_view,name='admin-view-doctor-certification'),
    path('admin-patient', views.admin_patient_view,name='admin-patient'),
    path('admin-view-patient', views.admin_view_patient_view,name='admin-view-patient'),
    path('delete-patient-from-hospital/<int:pk>', views.delete_patient_from_hospital_view,name='delete-patient-from-hospital'),
    path('update-patient/<int:pk>', views.update_patient_view,name='update-patient'),
    path('admin-add-patient', views.admin_add_patient_view,name='admin-add-patient'),
    path('admin-approve-patient', views.admin_approve_patient_view,name='admin-approve-patient'),
    path('approve-patient/<int:pk>', views.approve_patient_view,name='approve-patient'),
    path('reject-patient/<int:pk>', views.reject_patient_view,name='reject-patient'),
    path('admin-pharmacist', views.admin_pharmacist_view,name='admin-pharmacist'),
    path('admin-view-pharmacist', views.admin_view_pharmacist_view,name='admin-view-pharmacist'),
    path('admin-add-pharmacist', views.admin_add_pharmacist_view,name='admin-add-pharmacist'),
    path('admin-hospital', views.admin_hospital_view,name='admin-hospital'),
    path('admin-view-hospital', views.admin_view_hospital_view,name='admin-view-hospital'),
    path('admin-add-hospital', views.admin_add_hospital_view,name='admin-add-hospital'),
    path('delete-hospital/<int:pk>', views.delete_hospital_view,name='delete-hospital'),
    path('update-hospital/<int:pk>', views.update_hospital_view,name='update-hospital'),
    path('admin-view-profile', views.admin_profile_view),
    path('admin-lab_tech', views.admin_lab_tech_view,name='admin-lab_tech'),
    path('admin-view-lab_tech', views.admin_view_lab_tech_view,name='admin-view-lab_tech'),
    path('admin-add-lab_tech', views.admin_add_lab_tech_view,name='admin-add-lab_tech'),
    path('admin-view-schedule-doctor', views.admin_view_schedule_doctor_view,name='admin-view-schedule-doctor'),
    path('scheduling-doctor/<int:pk>', views.scheduling_doctor_view,name='scheduling-doctor'),
    path('admin-view-doctor-scheduled', views.admin_view_scheduled_doctor_view,name='admin-view-doctor-scheduled'),
  

]




#---------FOR DOCTOR RELATED URLS-------------------------------------

urlpatterns +=[

    path('doctor-dashboard', views.doctor_dashboard_view,name='doctor-dashboard'),
    path('doctor-patient', views.doctor_patient_view,name='doctor-patient'),
    path('doctor-view-patient', views.doctor_view_patient_view,name='doctor-view-patient'),
    path('doctor-delete-appointment',views.doctor_delete_appointment_view,name='doctor-delete-appointment'),
    path('delete-appointment/<int:pk>', views.delete_appointment_view,name='delete-appointment'),
    path('doctor-notification', views.doctor_notification_view,name='doctor-notification'),
    path('doctor-appointment', views.doctor_appointment_view,name='doctor-appointment'),
    path('doctor-prescription', views.doctor_prescription_view,name='doctor-prescription'),
    path('doctor-give-prescription', views.doctor_give_prescription_view,name='doctor-give-prescription'),
    path('doctor-view-prescription', views.doctor_view_prescription_view,name='doctor-view-prescription'),
    path('doctor-announcement', views.doctor_announcement_view,name='doctor-announcement'),
    path('doctor-post-announcement', views.doctor_post_announcement_view,name='doctor-post-announcement'),
    path('doctor-view-announcement', views.doctor_view_announcement_view,name='doctor-view-announcement'),
    path('doctor-delete-post-announcement/<int:pk>', views.delete_posted_announcement_view,name='doctor-delete-post-announcement'),
    path('doctor-view-appointment', views.doctor_view_appointment_view,name='doctor-view-appointment'),
    path('doctor-add-appointment', views.doctor_add_appointment_view,name='doctor-add-appointment'),
    path('doctor-approve-appointment', views.doctor_approve_appointment_view,name='doctor-approve-appointment'),
    path('approve-appointment/<int:pk>', views.approve_appointment_view,name='approve-appointment'),
    path('reject-appointment/<int:pk>', views.reject_appointment_view,name='reject-appointment'),
    path('doctor-laboratory', views.doctor_laboratory_view,name='doctor-laboratory'),
    path('doctor-order-lab', views.doctor_order_Lab_view,name='doctor-order-lab'),
    path('doctor-view-labOrder', views.doctor_view_labOrder_view,name='doctor-view-labOrder'),
    path('doctor-view-patient-diagnosis', views.doctor_patient_diagnosis_view,name='doctor-view-patient-symptom'),
    path('doctor-diagnosis-patient', views.doctor_patient_diagnosis,name='doctor-diagnosis-patient'),
    path('doctor-view-profile', views.doctor_profile_view),
    path('doctor-view-patient-labResult', views.doctor_patient_labResult_view),
    path('doctor-view-schedule', views.doctor_schedule_view),
    path('doctor-discharge-patient', views.discharge_patient),

   
]


#---------FOR PHARMACIST RELATED URLS-------------------------------------

urlpatterns +=[

        path('pharmacist-dashboard', views.pharmacist_dashboard_view,name='pharmacist-dashboard'),
        path('pharmacist-medicine', views.pharmacist_medicine_view,name='pharmacist-medicine'),
        path('pharmacist-view-medicine', views.pharmacist_view_medicine_view,name='pharmacist-view-medicine'),
        path('pharmacist-add-medicine', views.pharmacist_add_medicine_view,name='pharmacist-add-medicine'),
        path('pharmacist-view-profile', views.pharmacist_profile_view),
        path('pharmacist-prescription', views.pharmacist_prescription_view,name='pharmacist-prescription'),
        path('pharmacist-view-prescription', views.pharmacist_view_prescription_view,name='pharmacist-view-prescription'),
        path('pharmacist-request-payment/<int:pk>', views.pharmacist_request_payment_view,name='pharmacist-request-payment'),
        path('pharmacist-view-paymentRequest', views.pharmacist_view_paymentRequest_view,name='pharmacist-view-paymentRequest'),
        path('pharmacist-patient', views.pharmacist_patient_view,name='pharmacist-patient'),
        path('pharmacist-view-paymentRequest-status', views.pharmacist_view_paymentRequest_status_view,name='pharmacist-view-paymentRequest-status'),
        path('pharmacist-view-payed-patient', views.pharmacist_view_payed_patient_to_give_instruction_view,name='pharmacist-view-payed-patient'),
        path('pharmacist-giveMedicine-instruction/<int:pk>', views.pharmacist_give_medicine_instruction_view,name='pharmacist-giveMedicine-instruction'),
        path('pharmacist-view-instruction', views.pharmacist_view_medicine_instruction_view,name='pharmacist-view-instruction'),
        path('pharmacist-notification', views.pharmacist_notification_view,name='pharmacist-notification'),


]

#---------FOR LabTech RELATED URLS-------------------------------------

urlpatterns +=[

        path('labTech-dashboard', views.labTech_dashboard_view,name='labTech-dashboard'),
        path('labTech-laboratory', views.labTech_labOrder_view,name='labTech-laboratory'),
        path('labTech-view-labOrder', views.labTech_view_labOrder_view,name='labTech-view-labOrder'),
        path('labTech-request-payment/<int:pk>', views.labTech_request_payment_view,name='labTech-request-payment'),
        path('labTech-view-labRequest', views.labTech_view_labRequest_view,name='labTech-view-labRequest'),
        path('labTech-patient', views.labTech_patient_view,name='labTech-patient'),
        path('labTech-view-labRequest-status', views.labTech_view_labRequest_status_view,name='labTech-view-labRequest-status'),
        path('labTech-view-profile', views.labTech_profile_view),
        path('labTech-notification', views.labTech_notification_view),
        path('labTech-report-labResult', views.labTech_view_report_labResult,name='labTech-report-labResult'),
        path('labTech-report-patient-labResult/<int:pk>', views.labTech_report_patient_labResult,name='labTech-report-patient-labResult'),
        path('labTech-view-labResult', views.labTech_view_reported_patient_labResult, name='labTech-view-labResult'),



]



#---------FOR PATIENT RELATED URLS-------------------------------------
urlpatterns +=[

    path('patientsignup', views.patient_signup_view),
    path('patient-dashboard', views.patient_dashboard_view,name='patient-dashboard'),
    path('patient-appointment', views.patient_appointment_view,name='patient-appointment'),
    path('book-appointment', views.patient_book_appointment,name='book-appointment'),
    path('patient-view-appointment', views.patient_view_appointment_view,name='patient-view-appointment'),
    path('patient-view-appointment-details/<int:pk>', views.patient_book_apointement_details_views, name='patient-view-appointment-details'),
    path('patient-notification', views.patient_notification_view,name='patient-notification'),
    path('patient-view-labRequest', views.patient_view_labRequest_view,name='patient-view-labRequest'),
    path('patient-view-medicine', views.patient_view_medicine_view,name='patient-view-medicine'),
    path('patient-payment', views.patient_payment_view,name='patient-payment'),
    path('patient-medicalRecord', views.patient_medicalRecord_view,name='patient-medicalRecord'),
    path('patient-view-symptom', views.patient_view_symptom_view,name='patient-view-symptom'),
    path('patient-view-payment-method', views.patient_view_payment_method_view),
    path('patient-generate-bill/<int:pk>', views.patient_view_generate_bill_view,name='patient-generate-bill'),
    path('patient-generate-bill-forMedicine/<int:pk>', views.patient_view_generate_bill_forMedicine_view,name='patient-generate-bill-forMedicine'),
    path('patient-final-bill', views.patient_view_final_bill_view),
    path('download-pdf/<int:pk>', views.download_pdf_view,name='download-pdf'),
    path('patient-view-profile', views.patient_profile_view),
    path('patient-read-instruction', views.patient_read_instruction_to_use_medicine,name='patient-read-instruction'),


]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)