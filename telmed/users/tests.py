# users/tests.py

from django.test import TestCase
from .models import Doctor, CustomUser
from .serializers import DoctorSerializer

class DoctorSerializerTest(TestCase):
    def test_serialization(self):
        user = CustomUser.objects.create(email='doctor@example.com', is_doctor=True)
        doctor = Doctor.objects.create(
            user=user,
            first_name='John',
            last_name='Doe',
            area_of_specialization='Cardiology',
            location='New York',
            star_ranking=85,
            degree='MD',
            phone_number='1234567890'
        )
        serializer = DoctorSerializer(doctor)
        expected_data = {
            'id': doctor.id,
            'user': {
                'id': user.id,
                'email': 'doctor@example.com',
                'is_doctor': True,
                'is_patient': False
            },
            'first_name': 'John',
            'last_name': 'Doe',
            'area_of_specialization': 'Cardiology',
            'location': 'New York',
            'star_ranking': 85,
            'degree': 'MD',
            'phone_number': '1234567890',
            'hospital_name': None
        }
        self.assertEqual(serializer.data, expected_data)
