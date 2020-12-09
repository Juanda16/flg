from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Donation(models.Model):
    valueDonation=models.BigIntegerField(null=False,blank=False,editable=False)
    dateDonation = models.DateTimeField(auto_now_add=True,null=False,blank=False,editable=False)
    statusTransactionState= models.BooleanField()
    legalState = models.BooleanField()
    donorId = models.CharField(max_length=15, null=True, blank=False)
       
    def __str__(self):
        """
        String para representar el Objeto 
        """
        return 'Identificación del donante: %s Fecha de la donación: %s Valor de la donación: %s Transacción exitosa:%s Donación legalizada: %s \n' % (self.donorId,self.dateDonation,self.valueDonation,self.statusTransactionState,self.legalState)


class Fund(models.Model):
    valueFund=models.BigIntegerField(null=True,blank=False,editable=False)
    registerFund = models.TextField(max_length=10,null=False,blank=False,auto_created=True,unique=True)