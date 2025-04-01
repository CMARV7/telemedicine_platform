from rest_framework import serializers
from .models import CustomUser, Doctor, Patient,Appointment

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializes the CustomUser model for basic user information.
    """
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'is_doctor', 'is_patient']

class DoctorSerializer(serializers.ModelSerializer):
    """
    Serializes the Doctor model, including nested user data and custom validation.
    """
    user = CustomUserSerializer()  # Nested serializer for user details

    class Meta:
        model = Doctor
        fields = [
            'id', 'user', 'first_name', 'last_name', 'area_of_specialization',
            'location', 'star_ranking', 'degree', 'phone_number', 'hospital_name'
        ]

    def validate_star_ranking(self, value):
        """
        Ensures the star ranking is within a valid range.
        """
        if not (0 <= value <= 100):
            raise serializers.ValidationError("Star ranking must be between 0 and 100.")
        return value

    def create(self, validated_data):
        """
        Handles creation of a Doctor object along with its related CustomUser.
        """
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create(**user_data)  # Create CustomUser
        doctor = Doctor.objects.create(user=user, **validated_data)  # Create Doctor
        return doctor

class PatientSerializer(serializers.ModelSerializer):
    """
    Serializes the Patient model for patient-related data.
    """
    class Meta:
        model = Patient
        fields = [
            'id', 'user', 'first_name', 'middle_name', 'last_name',
            'email', 'phone', 'address', 'health_issues'
        ]


class AppointmentSerializer(serializers.ModelSerializer):
    """
    Serializer for Appointment model.
    """
    class Meta:
        model = Appointment
        fields = '__all__'