from app.models.donation import Donation
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from django.views import View
from django.http import QueryDict
from app.services.donationService import gettingDonation, postingDonation, puttingDonation, deletingDonation
import json
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout



#Views here.
#def index(request):
 #       return HttpResponse({'mssg': 'Donation index'})


class DonationView(View): # define an especfic Donotion CRUD
    def get(self, request, *args, **kwargs): #get
        donation = gettingDonation(id=kwargs['pk'])
        return HttpResponse(donation)

        
    def post(self, request, *args, **kwargs): # A especific Donation cant be posted
        return HttpResponse("Method not implemented ")

   
    def put(self, request, *args, **kwargs): #put
        id = kwargs['pk']
        donation = puttingDonation(request, id)
        return HttpResponse(donation)

    def delete(self, request, **kwargs): # A especific Donation cant be deleted
        return HttpResponse("Method not implemented") 

class DonationsView(View): # define Donotions CRUD

   def get(self, request, *args, **kwargs): #get
    
    return HttpResponse(Donation.objects.all())

   
   def post(self, request, *args, **kwargs):#post
      donation=postingDonation(request)
      return HttpResponse(donation)

   def put(self, request, *args, **kwargs): ## A generic Donate cant be puted

        return HttpResponse("Method not implemented ")

   def delete(self, request, *args, **kwargs): # A generic Donate cant be deleted

        return HttpResponse("Method not implemented")