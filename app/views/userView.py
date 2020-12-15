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
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from app.serializers import DonorSerializer
from rest_framework import viewsets, permissions



# Views here.
def index(request):
    #if not request.user.is_authenticated:
        return HttpResponse({'mssg': 'User index'})

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        #login(request, user)
        return HttpResponseRedirect("/donor/loggedin/")
    else:
        return HttpResponseRedirect("/donor/invalid/")


def logout_view(request):

    #logout(request)
    auth.logout(request)
    return HttpResponseRedirect("/donor/loggedout/")       
    

#@csrf_exempt
def get_data(request):
    data = Donor.objects.all()
    if request.method == 'GET':
        serializer = DonorSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
 
class DonorView(View): # define an especfic Donor CRUD

    
    def get(self, request, *args, **kwargs): #get
        
        #if user.is_authenticated:
        donor = gettingUser(id=kwargs['pk'])
        serializer = DonorSerializer(donor)
        
        return JsonResponse(serializer.data, safe=False)
        
    
        
    def post(self, request, *args, **kwargs): # A especific Donor cant be posted

        return HttpResponse("Method not implemented ")

    @login_required
    def put(self, request, *args, **kwargs): #put
        id = kwargs['pk']
        donor = puttingUser(request, id)
        return HttpResponse(donor)

    @login_required
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

class DonorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer
    
    #permission_classes = [permissions.IsAuthenticated]  
        
