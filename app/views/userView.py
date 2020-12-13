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
    

#@csrf_exempt
def get_data(request):
    data = Donor.objects.all()
    if request.method == 'GET':
        serializer = DonorSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'PUT', 'DELETE'])
def donor_detail(request, pk):
    # find tutorial by pk (id)
    try:
        donor = Donor.objects.get(pk=pk)
    except Donor.DoesNotExist:
        return JsonResponse({'message': 'The donor does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        donorSerializer = DonorSerializer(donor)
        return JsonResponse(donorSerializer.data)

    elif request.method == 'PUT': 
         donor_data = JSONParser().parse(request) 
         donorSerializer = DonorSerializer(donor, data=donor_data) 
         if donorSerializer.is_valid(): 
             donorSerializer.save() 
             return JsonResponse(donorSerializer.data) 
         return JsonResponse(donorSerializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        donor.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


class DonorView(View): # define an especfic Donor CRUD

    def get(self, request, *args, **kwargs): #get

        try:
            donor = Donor.objects.get(id=kwargs['pk'])
            donorSerializer = DonorSerializer(donor)
            return JsonResponse(donorSerializer.data)

        except Donor.DoesNotExist:
            return JsonResponse({'message': 'The donor does not exist'}, status=status.HTTP_404_NOT_FOUND)


    def post(self, request, *args, **kwargs): # A especific Donor cant be posted

        donor_data = JSONParser().parse(request)
        donorSerializer = DonorSerializer(data=donor_data)
        if donorSerializer.is_valid():
            donorSerializer.save()
            return JsonResponse(donorSerializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(donorSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs): #put
        try:
            donor = Donor.objects.get(id=kwargs['pk'])
            donor_data = JSONParser().parse(request) 
            donorSerializer = DonorSerializer(donor, data=donor_data) 
            if donorSerializer.is_valid(): 
                donorSerializer.save() 
                return JsonResponse(donorSerializer.data) 
            return JsonResponse(donorSerializer.errors, status=status.HTTP_400_BAD_REQUEST) 

        except Donor.DoesNotExist:
            return JsonResponse({'message': 'The donor does not exist'}, status=status.HTTP_404_NOT_FOUND)


    def delete(self, request, **kwargs): #delete
        try:
            donor = Donor.objects.get(id=kwargs['pk'])
            donor.delete() 
            return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        except Donor.DoesNotExist:
            return JsonResponse({'message': 'The donor does not exist'}, status=status.HTTP_404_NOT_FOUND)


""" class DonorView(View): # define an especfic Donor CRUD

    
    def get(self, request, *args, **kwargs): #get
        
        #if user.is_authenticated:
        donor = gettingUser(    )
        serializer = DonorSerializer(donor)
        
        return JsonResponse(serializer.data, safe=False)
        
    
    @csrf_exempt    
    def post(self, request, *args, **kwargs): # A especific Donor cant be posted

        return HttpResponse("Method not implemented ")

    #@login_required
    @csrf_exempt
    def put(self, request, *args, **kwargs): #put
        id = kwargs['pk']
        donor = puttingUser(request, id)
        return HttpResponse(donor)

    #@login_required
    def delete(self, request, **kwargs): #delete
        id = kwargs['pk']
        deletingUser(request, id)
        return HttpResponse("El usuario ha sido eliminado") """


class DonorsView(View): # define Donors CRUD

    def get(self, request, *args, **kwargs):  # get
        donors= Donor.objects.all()
        #return HttpResponse(donors)
        serializer = DonorSerializer(donors)
        #serializer = DonorSerializer('\n'.join([donor.documentId for donor in donors]))
        
        return JsonResponse(serializer.data,safe=False)

    @csrf_exempt
    def post(self, request, *args, **kwargs):  # post
        donor = postingUser(request)
        return HttpResponse(donor)

    
    def options(self, request):
        allowed_methods = "'get', 'post', 'put', 'delete', 'options'"
        response = HttpResponse()
        response['allow'] = ','.join([allowed_methods])
        return response   

    @csrf_exempt
    def put(self, request, *args, **kwargs): ## A generic Donor cant be puted

        return HttpResponse("Method not implemented ")

    @csrf_exempt
    def delete(self, request, *args, **kwargs): # A generic Donor cant be delete

        return HttpResponse("Method not implemented")

class DonorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed  or edited.
    """
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer
    
    #permission_classes = [permissions.IsAuthenticated]  
        
