from django.contrib import admin
from .models import CustomUser, Doctor, Patient

# Custom admin for CustomUser
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """
    Admin configuration for the CustomUser model.
    """
    list_display = ('id', 'email', 'is_doctor', 'is_patient', 'is_staff')
    list_filter = ('is_doctor', 'is_patient', 'is_staff')
    search_fields = ('email',)
    ordering = ('id',)

# Custom admin for Doctor
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Doctor model.
    """
    list_display = ('id', 'first_name', 'last_name', 'area_of_specialization', 'star_ranking', 'hospital_name')
    list_filter = ('area_of_specialization', 'location')
    search_fields = ('first_name', 'last_name', 'area_of_specialization', 'hospital_name')
    ordering = ('id',)

# Custom admin for Patient
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Patient model.
    """
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone', 'address', 'health_issues')
    list_filter = ('address',)
    search_fields = ('first_name', 'last_name', 'email', 'health_issues')
    ordering = ('id',)

