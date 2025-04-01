from django.contrib import admin
from .models import Hospital

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'areas_of_specialization', 'rating')  # Corrected field name
    search_fields = ('name', 'location', 'areas_of_specialization')  # Corrected field name
    list_filter = ('location', 'areas_of_specialization')  # Corrected field name
    ordering = ('name',)
