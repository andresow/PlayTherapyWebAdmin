from django.db import models
from apps.patients.models import *
from django_select2.forms import ModelSelect2MultipleWidget, Select2MultipleWidget

class Entity(models.Model):
    name = models.CharField(max_length=64)
    
    def __unicode__(self):
        return self.id
    def __str__(self):
        return self.name
        
class TypeDiagnostic(models.Model):
    name = models.CharField(max_length=64, unique=True)
    
    def __unicode__(self):
        return self.id
    def __str__(self):
        return self.name
    
class Diagnostic(models.Model):
    code = models.CharField(max_length=64, unique=True)
    name = models.TextField()
    type_diagnostic = models.ForeignKey(TypeDiagnostic, on_delete=models.CASCADE)
    
    def __unicode__(self):
        return self.id

    def __str__(self):
        return self.name
        
class Patient(models.Model):   
    
    id_type = models.CharField(max_length=64)
    id_num = models.CharField(max_length=64, unique=True) # Primary key
    name = models.CharField(max_length=64,)
    lastname = models.CharField(max_length=64)
    genre = models.CharField(max_length=64)
    occupation = models.CharField(max_length=64)
    birthday = models.DateField()
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    list_diagnostic = models.ForeignKey(Diagnostic, on_delete=models.CASCADE)
    
    def __unicode__(self):
        return self.id_num + ' - ' + self.name
    def __str__(self):
        return self.name