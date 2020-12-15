from django.shortcuts import render
from app.models.donor import Donor
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone
from django.views import View
from django.http import QueryDict
from app.services.userService import gettingUser, postingUser, puttingUser, deletingUser
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from app.serializers import DonorSerializer, UserSerializer, UserLoginSerializer
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
        
        donor = gettingUser(id=kwargs['pk'])
        return donor

    def post(self, request, *args, **kwargs): # A especific Donor cant be posted
<<<<<<< HEAD

        donor_data = JSONParser().parse(request)
        print("donor_data,donor_datadonor_datadonor_datadonor_datadonor_datadonor_datadonor_datadonor_datadonor_datadonor_datadonor_datadonor_datadonor_datadonor_datadonor_datadonor_datadonor_datadonor_datadonor_datadonor_datadonor_datadonor_datadonor_datadonor_datadonor_datadonor_data")
        donorSerializer = DonorSerializer(data=donor_data)
        if donorSerializer.is_valid():
            donorSerializer.save()
            return JsonResponse(donorSerializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(donorSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
=======
        
        return HttpResponse("Method not implemented ")
>>>>>>> a7313b46315ccb4ed8096b7912d0917a2d41018e

    def put(self, request, *args, **kwargs): #put
        
        id = kwargs['pk']
        donor = puttingUser(request,id)
        return donor

    def delete(self, request, **kwargs): #delete
        
        id = kwargs['pk']
        donor = deletingUser(id)
        return donor

class DonorsView(View): # define Donors CRUD

   def get(self, request, *args, **kwargs): #get
        
        donors= Donor.objects.all()
                
        documentId = request.GET.get('documentId', None)
        if documentId is not None:
            donors = donors.filter(documentId__icontains=documentId)
        
        donorsSerializer = DonorSerializer(donors, many=True)
        return JsonResponse(donorsSerializer.data, safe=False)

   def post(self, request, *args, **kwargs):  # post
        
        donor = postingUser(request)
        return donor

   def put(self, request, *args, **kwargs): ## A generic Donor cant be puted

        return HttpResponse("Method not implemented ")

   def delete(self, request, *args, **kwargs): # A generic Donor cant be delete

        return HttpResponse("Method not implemented")

class LoginUserView(View):

    def post(self, request, *args, **kwargs):
        """User sign in."""
        user_data = JSONParser().parse(request)
        serializer = UserLoginSerializer(data=user_data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserSerializer(user).data,
            'access_token': token
        }
        return JsonResponse(data, status=status.HTTP_201_CREATED)
        
