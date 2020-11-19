from django.shortcuts import render
from app.models import Donor
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date


# Create your views here.

def index(request):
   return render(request, 'app/index.html', {})

def donor(request):
    
   # if request.method == 'GET':
       

    if request.method == 'POST':
        firstname = request.POST["first_name"]
        lastname = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        username = firstname+lastname
        user = User.objects.create_user(username, email, password)
        Donor.objects.create(user=user, documentType="cuentanos de tí",documentId="" , legalNature="")
        
    
        return ()
        
