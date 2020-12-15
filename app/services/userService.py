from app.models.donor import Donor
from django.contrib.auth.models import User
from django.http import QueryDict
from datetime import date
from app.serializers import DonorSerializer
from rest_framework import viewsets, permissions
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status


# business logic

def gettingUser(id):
    try:
        donor = Donor.objects.get(id=id)
        donorSerializer = DonorSerializer(donor)
        return JsonResponse(donorSerializer.data)

    except Donor.DoesNotExist:
        return JsonResponse({'message': 'The donor does not exist'}, status=status.HTTP_404_NOT_FOUND)


def postingUser(request):
    donor_data = JSONParser().parse(request)
    donorSerializer = DonorSerializer(data=donor_data)
    if donorSerializer.is_valid():
        donorSerializer.save()
        return JsonResponse(donorSerializer.data, status=status.HTTP_201_CREATED) 
    return JsonResponse(donorSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


def puttingUser(request,id):
    try:
        donor = Donor.objects.get(id=id)
        donor_data = JSONParser().parse(request) 
        donorSerializer = DonorSerializer(donor, data=donor_data) 
        if donorSerializer.is_valid():  
            donorSerializer.save() 
            return JsonResponse(donorSerializer.data) 
        return JsonResponse(donorSerializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    except Donor.DoesNotExist:
        return JsonResponse({'message': 'The donor does not exist'}, status=status.HTTP_404_NOT_FOUND)

def deletingUser(id):
    try:
        donor = Donor.objects.get(id=id)
        donor.delete() 
        return JsonResponse({'message': 'Donor was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except Donor.DoesNotExist:
       return JsonResponse({'message': 'The donor does not exist'}, status=status.HTTP_404_NOT_FOUND)

