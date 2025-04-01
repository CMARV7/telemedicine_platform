from rest_framework import serializers
from .models import Hospital

class HospitalSerializer(serializers.ModelSerializer):
    """
    Serializer for the Hospital model.
    Converts model instances into JSON format and validates data.
    """
    class Meta:
        model = Hospital
        fields = ['id', 'name', 'location', 'areas_of_specialization', 'rating']
