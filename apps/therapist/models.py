from django.db import models
from django.contrib.auth.models import User

class Therapist(User):

    CEDULA = 'Cédula de ciudadania'
    TARJETA = 'Tarjeta de identidad'
    PASAPORTE = 'Número de pasaporte'
    EXTRANJERIA = 'Cédula de extranjeria'
    
    ID_CHOICES = [(CEDULA, CEDULA), 
    (TARJETA, TARJETA),
    (PASAPORTE, PASAPORTE),
    (EXTRANJERIA, EXTRANJERIA)]
    
    MALE= 'Masculino'
    FEMALE = 'Femenino'
    GENRE_CHOICES = [(MALE, 'Masculino'),(FEMALE, 'Femenino')]
    
    name = models.CharField(max_length=64, verbose_name='Nombre')
    lastname = models.CharField(max_length=64, verbose_name='Apellido')
    id_type = models.CharField(max_length=64, choices=ID_CHOICES, verbose_name='Tipo de identificación')
    genre = models.CharField(max_length=64, choices=GENRE_CHOICES, verbose_name='Género')
    
    def __unicode__(self):
        return self.name + " " + self.lastname