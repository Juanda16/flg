from app.models.donation import Donation
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from django.views import View
from django.http import QueryDict
from app.services.donationService import gettingDonation, postingDonation, puttingDonation, deletingDonation
import json
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from app.serializers import DonationSerializer
from rest_framework import viewsets, permissions
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status


# Views here.
# def index(request):
#       return HttpResponse({'mssg': 'Donation index'})


class DonationView(View):  # define an especfic Donotion CRUD

    def get(self, request, *args, **kwargs):  # get
        donation = gettingDonation(id=kwargs['pk'])
        return donation

    def post(self, request, *args, **kwargs):  # A especific Donation cant be posted
        return HttpResponse("Method not implemented ")

    def put(self, request, *args, **kwargs):  # put
        id = kwargs['pk']
        donation = puttingDonation(request, id)
        return donation

    def delete(self, request, **kwargs):  # A especific Donation cant be deleted
        id = kwargs['pk']
        donation = deletingDonation(id)
        return donation


class DonationsView(View):  # define Donations CRUD

    def get(self, request, *args, **kwargs):  # get
        donations = Donation.objects.all()
        donorId = request.GET.get('donorId',None)
        if donorId is not None:
            donations = donations.filter(donorId__icontains=donorId)

        donationsSerializer = DonationSerializer(donations, many=True)
        return JsonResponse(donationsSerializer.data, safe=False)

    def post(self, request, *args, **kwargs):  # post
        donation = postingDonation(request)
        return donation

    def put(self, request, *args, **kwargs):  # A generic Donate cant be puted

        return HttpResponse("Method not implemented ")

    def delete(self, request, *args, **kwargs):  # A generic Donate cant be deleted

        return HttpResponse("Method not implemented")
