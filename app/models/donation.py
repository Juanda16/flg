from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Donation(models.Model):
    valueDonation=models.BigIntegerField(null=True,blank=True,editable=True)
    dateDonation = models.DateTimeField(auto_now_add=True,null=True,blank=True,editable=False)
    statusTransactionState= models.BooleanField(null=True,blank=True)
    legalState = models.BooleanField(null=True,blank=True)
    donorId = models.CharField(max_length=15, null=True, blank=True)
       
    def __str__(self):
        """
        String para representar el Objeto 
        """
        return 'Identificación del donante: %s Fecha de la donación: %s Valor de la donación: %s Transacción exitosa:%s Donación legalizada: %s \n' % (self.donorId,self.dateDonation,self.valueDonation,self.statusTransactionState,self.legalState)


class Fund(models.Model):
    valueFund=models.BigIntegerField(null=True,blank=False,editable=False)
    registerFund = models.TextField(max_length=10,null=False,blank=False,auto_created=True,unique=True)