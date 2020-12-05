from django.shortcuts import render
from app.models.donor import Donor
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from django.views import View
from django.http import QueryDict
from app.service import gettingUser, postingUser, puttingUser, deletingUser
import json
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
#from .serializers import DonorSerializer


# Views here.
def index(request):
    #if not request.user.is_authenticated:
        return HttpResponse({'mssg': 'User index'})

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse(user.username + " loggeado")
    else:
        return HttpResponse( {"message": "Invalid credentials."})


def logout_view(request):

    logout(request)
    return HttpResponse({"message": "Logged out."})        
    


class DonorView(View): # define an especfic Donor CRUD
    def get(self, request, *args, **kwargs): #get
        donor = gettingUser(id=kwargs['pk'])
        return HttpResponse(donor)

        
    def post(self, request, *args, **kwargs): # A especific Donor cant be posted

        return HttpResponse("Method not implemented ")

   
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
      donor=postingUser(request)
      return HttpResponse(donor)

   def put(self, request, *args, **kwargs): ## A generic Donor cant be puted

        return HttpResponse("Method not implemented ")

   def delete(self, request, *args, **kwargs): # A generic Donor cant be delete

        return HttpResponse("Method not implemented")
