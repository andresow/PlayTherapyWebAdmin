from django.db import models
from apps.patients.models import *

class FunctionalIndependenceMeasure(models.Model):

    date = models.DateField()
    goal = models.BooleanField(default=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
    UNO = 1
    DOS = 2 
    TRES = 3
    CUATRO = 4
    CINCO = 5
    SEIS = 6
    SIETE = 7
    NUMBER_CHOICES = [(UNO, UNO), (DOS, DOS), (TRES, TRES), (CUATRO, CUATRO), (CINCO, CINCO), (SEIS, SEIS), (SIETE, SIETE)]
    
    
    #selfcare
    eat =  models.IntegerField(choices=NUMBER_CHOICES)
    personal_clean =  models.IntegerField(choices=NUMBER_CHOICES)
    bath =  models.IntegerField(choices=NUMBER_CHOICES)
    dress_undress_sup =  models.IntegerField(choices=NUMBER_CHOICES)
    dress_undress_inf =  models.IntegerField(choices=NUMBER_CHOICES)
    bathUse =  models.IntegerField(choices=NUMBER_CHOICES)
    
    #potty training
    control_dregs =  models.IntegerField(choices=NUMBER_CHOICES)
    control_urine =  models.IntegerField(choices=NUMBER_CHOICES)
    
    #move
    tras_bed_chair = models.IntegerField(choices=NUMBER_CHOICES)
    tras_bath = models.IntegerField(choices=NUMBER_CHOICES)
    tras_shower = models.IntegerField(choices=NUMBER_CHOICES)
    
    #move 
    run_crawl_chair = models.IntegerField(choices=NUMBER_CHOICES)
    steps = models.IntegerField(choices=NUMBER_CHOICES)
    
    #comunication
    compresion = models.IntegerField(choices=NUMBER_CHOICES)
    expresion = models.IntegerField(choices=NUMBER_CHOICES)
    
    #social cognition
    social_inter = models.IntegerField(choices=NUMBER_CHOICES)
    problem_solve = models.IntegerField(choices=NUMBER_CHOICES)
    memory =  models.IntegerField(choices=NUMBER_CHOICES)
    
    def total(self):
        total = self.eat + self.personal_clean + self.bath + self.dress_undress_sup + self.dress_undress_inf + self.bathUse + self.control_dregs + self.control_urine
        total += self.tras_bed_chair + self.tras_bath + self.tras_shower + self.run_crawl_chair + self.steps + self.compresion
        total += self.expresion + self. social_inter + self.problem_solve + self.memory
        
        return total
        
    def __unicode__(self):
        return self.patient.id_num + ' ' + str(self.date)
    