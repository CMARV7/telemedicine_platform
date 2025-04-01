from django.urls import path
from .views import HospitalListCreateView, HospitalDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('hospitals/', HospitalListCreateView.as_view(), name='hospital-list-create'),
    path('hospitals/<int:pk>/', HospitalDetailView.as_view(), name='hospital-detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
