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
from app.services.userService import gettingUser, postingUser, puttingUser, deletingUser, userLogin
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from app.serializers import DonorSerializer, UserSerializer, UserLoginSerializer
from rest_framework import viewsets, permissions
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status




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
    
class DonorView(View): # define an especfic Donor CRUD

    def get(self, request, *args, **kwargs): #get

        donor = gettingUser(id=kwargs['pk'])
        return donor

        


    def post(self, request, *args, **kwargs): # A especific Donor cant be posted

        return JsonResponse({"status":"A especific Donor cant be posted"})

    def put(self, request, *args, **kwargs): #put
        id = kwargs['pk']
        donor = puttingUser(request,id)
        return donor


    def delete(self, request, **kwargs): #delete
        id = kwargs['pk']
        donor = deletingUser(id)
        return donor


class DonorsView(View): # define Donors CRUD

    def get(self, request, *args, **kwargs):  # get
        donors= User.objects.all()
                
        first_name = request.GET.get('first_name', None)
        if first_name is not None:
            donors = donors.filter(first_name__icontains=first_name)
        
        donorsSerializer = UserSerializer(donors, many=True)
        return JsonResponse(donorsSerializer.data, safe=False)

    def post(self, request, *args, **kwargs): # A especific Donor cant be posted

        donor = postingUser(request)
        return donor

    
    def options(self, request):
        allowed_methods = "'get', 'post', 'put', 'delete', 'options'"
        response = HttpResponse()
        response['allow'] = ','.join([allowed_methods])
        return response   

    
    def put(self, request, *args, **kwargs): ## A generic Donor cant be puted

        return JsonResponse({"status":"A generic Donor cant be putted"})

    
    def delete(self, request, *args, **kwargs): # A generic Donor cant be delete

        return JsonResponse({"status":"many donors cant be deleted"})

class LoginUserView(View):

    def post(self, request, *args, **kwargs):
        """User sign in."""
        response= userLogin(request)
        return response
        
