from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import (
    RegisterSerializer,
    PatientSerializer,
    DoctorSerializer,
    PatientDoctorMappingSerializer,
)
from .models import Patient, Doctor, PatientDoctorMapping


# 🔐 Register View
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


# 🔐 JWT Login View
class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)


# 🩺 Patient CRUD
class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Patient.objects.none()
        user = self.request.user
        print("Authenticated user:", user)  # Debug
        return Patient.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# 👨‍⚕️ Doctor CRUD
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = (IsAuthenticated,)


# 🔗 Patient ↔ Doctor Mappings
class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        patient_id = self.kwargs.get('patient_id', None)
        if patient_id:
            return PatientDoctorMapping.objects.filter(patient_id=patient_id)
        return PatientDoctorMapping.objects.all()


# 🌐 Root Info View
class RootView(APIView):
    permission_classes = []

    def get(self, request):
        return Response({
            "message": "Welcome to the Healthcare Backend API",
            "note": "💡 To test all the endpoints visually, use Swagger UI at \"/swagger\" endpoint.",
            "endpoints": {
                "admin": "/admin/",
                "auth_register": "/api/auth/register/",
                "auth_login": "/api/auth/login/",
                "patients": "/api/patients/",
                "doctors": "/api/doctors/",
                "mappings": "/api/mappings/"
            }
        }, status=status.HTTP_200_OK)
