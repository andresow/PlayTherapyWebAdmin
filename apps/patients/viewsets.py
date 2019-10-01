from rest_framework import viewsets
from .models import Patient,Entity,Diagnostic,TypeDiagnostic
from .serializer import PatientSerializer, EntitySerializer, DiagnosticSerializer, TypeDiagnosticSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer

class DiagnosticViewSet(viewsets.ModelViewSet):
    queryset = Diagnostic.objects.all()
    serializer_class = DiagnosticSerializer

class TypeDiagnosticViewSet(viewsets.ModelViewSet):
    queryset = TypeDiagnostic.objects.all()
    serializer_class = TypeDiagnosticSerializer