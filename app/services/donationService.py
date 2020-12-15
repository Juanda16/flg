from app.models.donation import Donation,Fund
from django.contrib.auth.models import User
from app.models.donor import Donor
from django.http import QueryDict
from datetime import date
from app.serializers import DonationSerializer
from rest_framework import viewsets, permissions
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
import datetime



# business logic

def gettingDonation(id):
   
    try:
        donation = Donation.objects.get(donorId=id)
        donationSerializer = DonationSerializer(donation)
        return JsonResponse(donationSerializer.data)

    except Donation.DoesNotExist:
        return JsonResponse({'message': 'The donation does not exist'}, status=status.HTTP_404_NOT_FOUND)


def postingDonation(request):
    donation_data = JSONParser().parse(request)
    donationSerializer = DonationSerializer(data=donation_data)
    if donationSerializer.is_valid():
        donationSerializer.save()
        return JsonResponse(donationSerializer.data, status=status.HTTP_201_CREATED) 
    return JsonResponse(donationSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

def puttingDonation(request,id):
    try:        
        donation = Donation.objects.get(id=id)
        donation_data = JSONParser().parse(request) 
        donationSerializer = DonationSerializer(donation, data=donation_data) 
        if donationSerializer.is_valid():  
            donationSerializer.save() 
            return JsonResponse(donationSerializer.data) 
        return JsonResponse(donationSerializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    except Donation.DoesNotExist:
            return JsonResponse({'message': 'The donation does not exist'}, status=status.HTTP_404_NOT_FOUND)
    

def deletingDonation(id):
    try:
        donation = Donation.objects.get(id=id)
        donation.delete() 
        return JsonResponse({'message': 'Donation was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except Donation.DoesNotExist:
        return JsonResponse({'message': 'The donation does not exist'}, status=status.HTTP_404_NOT_FOUND)


def checkBalance():
    date = datetime.now()
    timeLastSend = sendMoney()
    if (timeLastSend < Donation.dateDonation and Donation.dateDonation < date):
        balance = Donation.objects.all().aggregate(sum('valueDonation'))
    return balance

def sendMoney():
    actualBalance = checkBalance()
    fund = Fund.objects.get(id=1)
    actualFund = fund.valueFundn + actualBalance
    timeLastSend = datetime.now()
    return timeLastSend
    #return "Exit send to fund"
    

    
