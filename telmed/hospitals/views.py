from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import generics
from .models import Hospital
from .serializers import HospitalSerializer
from .permissions import IsAdminOrReadOnly

class HospitalListCreateView(generics.ListCreateAPIView):
    """
    API view to retrieve a list of hospitals and allow authenticated users to create a new hospital.
    """
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """
        Allow only authenticated users to create a hospital.
        """
        serializer.save()

class HospitalDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a specific hospital.
    Admin users can update and delete hospital records.
    """
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    permission_classes = [IsAdminOrReadOnly]
