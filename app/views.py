from django.shortcuts import render
from app.models import Donor
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from django.views import View
from django.http import QueryDict
from app.service import gettingUser,postingUser,puttingUser,deletingUser
#import json

class DonorView(View):
        def get(self, request,*args,**kwargs):
                donor = gettingUser(id=kwargs['pk'])
                return HttpResponse(donor)
    

        def post(self, request, *args, **kwargs):
                donor = postingUser(request)
                return HttpResponse(donor)
                #return HttpResponsedonor)

        def put(self,request,*args,**kwargs):
                id=kwargs['pk']
                donor=puttingUser(request,id)
                return HttpResponse(donor)

        def delete(self,request,**kwargs):
               id=kwargs['pk']
               deletingUser(request,id)
               return HttpResponse("El usuario ha sido eliminado") 