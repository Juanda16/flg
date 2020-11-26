from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

# Entity.


class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    documentType = models.CharField(max_length=15,null=True,blank=False)
    documentId= models.CharField(max_length=15, null=True, blank=False)
    legalNature = models.CharField(max_length=64, null=True,blank=True)
    mobile = models.CharField(max_length=64, null=True,blank=True)
       
    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
<<<<<<< HEAD
        return 'Nombre:%s Apellido:%s Username:%s Documento:%s' % (self.user.first_name, self.user.last_name, self.user.username, self.documentId)

=======
        return 'nombre: %s apellido: %s username:%s #docuemento: %s' % (self.user.first_name, self.user.last_name, self.user.username, self.documentId)
>>>>>>> db0b87fec8308048d0247d3eedb31541a1628ca7


    

