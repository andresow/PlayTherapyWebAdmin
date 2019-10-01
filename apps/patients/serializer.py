from rest_framework import serializers
from .models import Patient,Entity,Diagnostic,TypeDiagnostic

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = '__all__'
        
class TypeDiagnosticSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeDiagnostic
        fields = '__all__'

class DiagnosticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostic
        fields = '__all__'


