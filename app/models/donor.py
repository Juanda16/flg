from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User, Group
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

# Entity.


class Donor(models.Model):  #donor model 
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True) # A user has a donor
    documentType = models.CharField(max_length=15,null=True,blank=False)
    documentId= models.CharField(max_length=15, null=True, blank=False)
    #legalNature = models.CharField(max_length=64, null=True,blank=True)
    legalNature = models.BooleanField(default=False)
    mobile = models.CharField(max_length=64, null=True,blank=True)
       
    def __str__(self):
        """
        String para representar el Objeto 
        """
        return 'nombre: %s apellido: %s username:%s #docuemento: %s \n' % (self.user.first_name, self.user.last_name, self.user.username, self.documentId)
    

