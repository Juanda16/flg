from django.shortcuts import render
from app.models import Donor
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from django.views import View
from django.http import QueryDict
<<<<<<< HEAD
from app.service import *
=======
from app.service import gettingUser, postingUser, puttingUser, deletingUser
>>>>>>> 1fb8fb92c5b48b47d408e0c487b1970b0df17869
import json
from rest_framework import routers, serializers, viewsets
from .serializers import DonorSerializer


# Views here.

<<<<<<< HEAD
class DonorView(View):
   def get(self, request, *args, **kwargs):
      donor = gettingUser (id = kwargs['pk'])
      return HttpResponse(donor)
      
=======
class DonorView(View): # define an especfic Donor CRUD
    def get(self, request, *args, **kwargs): #get
        donor = gettingUser(id=kwargs['pk'])
        return HttpResponse(donor)

        
    def post(self, request, *args, **kwargs): # A especific Donor cant be posted

        return HttpResponse("Method not implemented ")
>>>>>>> 1fb8fb92c5b48b47d408e0c487b1970b0df17869

   
    def put(self, request, *args, **kwargs): #put
        id = kwargs['pk']
        donor = puttingUser(request, id)
        return HttpResponse(donor)

    def delete(self, request, **kwargs): #delete
        id = kwargs['pk']
        deletingUser(request, id)
        return HttpResponse("El usuario ha sido eliminado")


class DonorsView(View): # define Donors CRUD

   def get(self, request, *args, **kwargs): #get
    
    return HttpResponse(Donor.objects.all())

   
   def post(self, request, *args, **kwargs):#post
      userName = request.POST["userName"]
      email = request.POST["email"]
      password = request.POST["password"]
      user = User.objects.create_user(userName, email, password)
      Donor.objects.create(user=user, documentType=request.POST["documentType"], documentId=request.POST["documentId"])
      return HttpResponse(user)

   def put(self, request, *args, **kwargs): ## A generic Donor cant be puted

<<<<<<< HEAD
=======
        return HttpResponse("Method not implemented ")
>>>>>>> 1fb8fb92c5b48b47d408e0c487b1970b0df17869

   def delete(self, request, *args, **kwargs): # A generic Donor cant be delete

        return HttpResponse("Method not implemented")
