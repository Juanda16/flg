from django.shortcuts import render
from app.models import Donor
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from django.views import View
from django.http import QueryDict
<<<<<<< HEAD
from app.service import gettingUser,postingUser,puttingUser,deletingUser
#import json
=======
from app.service import *
import json
from django.http import JsonResponse



# Views here.
>>>>>>> db0b87fec8308048d0247d3eedb31541a1628ca7

class DonorView(View):
<<<<<<< HEAD
        def get(self, request,*args,**kwargs):
                donor = gettingUser(id=kwargs['pk'])
                return HttpResponse(donor)
    

        def post(self, request, *args, **kwargs):
                donor = postingUser(request)
                return HttpResponse(donor)
                #return HttpResponsedonor)
=======
   def get(self, request, *args, **kwargs):
      donor = gettingUser (id = kwargs['pk'])
      return HttpResponse(donor)
      

   
   def post(self, request, *args, **kwargs):
      userName= request.POST["userName"]
      email = request.POST["email"]
      password = request.POST["password"]
      user = User.objects.create_user(userName, email, password)
      Donor.objects.create(user=user,documentType=request.POST["documentType"], documentId=request.POST["documentId"])
      
      

      return HttpResponse(user)

   def put(self,request,*args,**kwargs):
      put = QueryDict(request.body)
      
      try:
         _userid = kwargs['pk']
         user = User.objects.get(id=_userid)
         user.username = put.get('username')
         user.first_name = put.get('first_name')
         user.last_name = put.get('last_name')
         user.email = put.get('email')
         user.password = put.get('password')
         user.save()
         donor = Donor.objects.get(user_id=_userid)
         donor.documentType = put.get('documentType')
         donor.documentId = put.get('documentId')
         donor.save()

         return HttpResponse(user)

      except User.DoesNotExist:

         return HttpResponse("user doesn´t exist")
      
      

      
    
    

>>>>>>> db0b87fec8308048d0247d3eedb31541a1628ca7

        def put(self,request,*args,**kwargs):
                id=kwargs['pk']
                donor=puttingUser(request,id)
                return HttpResponse(donor)

        def delete(self,request,**kwargs):
               id=kwargs['pk']
               deletingUser(request,id)
               return HttpResponse("El usuario ha sido eliminado") 