from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CustomUserViewSet,
    DoctorViewSet,
    PatientViewSet,
    AppointmentViewSet  # ✅ Import AppointmentViewSet
)

# Register all viewsets
router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')
router.register(r'doctors', DoctorViewSet, basename='doctor')
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'appointments', AppointmentViewSet, basename='appointment')  # ✅ Add this

urlpatterns = [
    path('', include(router.urls)),
]
