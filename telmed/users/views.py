from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import CustomUser, Doctor, Patient, Appointment
from .serializers import CustomUserSerializer, DoctorSerializer, PatientSerializer, AppointmentSerializer
from .permissions import IsAdmin, IsDoctor, IsPatient


class CustomUserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing CustomUser instances.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class DoctorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to view and search doctors.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    # Enable filtering and search
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['area_of_specialization', 'location', 'hospital_name']
    search_fields = ['first_name', 'last_name']


class PatientViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Patient instances.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    

class AppointmentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Appointments.
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def get_permissions(self):
        """
        Define permissions based on role.
        """
        if self.action in ['list', 'retrieve']:  # Doctors & Admins can view
            return [permissions.IsAuthenticated(), IsDoctor() | IsAdmin()]
        elif self.action == 'create':  # Patients can book an appointment
            return [permissions.IsAuthenticated(), IsPatient()]
        elif self.action in ['update', 'destroy']:  # Only doctors can update
            return [permissions.IsAuthenticated(), IsDoctor()]
        return super().get_permissions()
