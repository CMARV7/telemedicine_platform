from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings  # ✅ Import settings

class CustomUser(AbstractUser):
    """
    Custom user model extending AbstractUser.
    """
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    ]

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='patient')
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.email} ({self.role})"


class Doctor(models.Model):
    """
    Doctor model linked to CustomUser.
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    area_of_specialization = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    star_ranking = models.PositiveIntegerField(default=0)
    degree = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    hospital_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"


class Patient(models.Model):
    """
    Patient model linked to CustomUser.
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    health_issues = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Appointment(models.Model):
    """
    Model to store doctor appointment details.
    Patients can book appointments with doctors.
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, related_name='appointments')
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Appointment with Dr. {self.doctor.user.first_name} on {self.date} at {self.time}"
