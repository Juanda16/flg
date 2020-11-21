from django.shortcuts import render
from app.models import Donor
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from django.views import View
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def index(request):
   return render(request, 'app/index.html', {})

 
class DonorView(View):
   def get(self, request, *args, **kwargs):
      return HttpResponse('Esto es un get correcto!')

   #@csrf_exempt
   def post(self, request, *args, **kwargs):
      userName= request.POST["userName"]
      email = request.POST["email"]
      password = request.POST["password"]
      user = User.objects.create_user(userName, email, password)
      Donor.objects.create(user=user,documentType="Cedula", documentId="123456")
      

      return HttpResponse(user)


# def donor(request):
    
#    # if request.method == 'GET':
       

#     if request.method == 'POST':
#         #firstname = request.POST["first_name"]
#         #lastname = request.POST["last_name"]
#         email = request.POST["email"]
#         password = request.POST["password"]
#         username = email
#         user = User.objects.create_user(username, email, password)
#         Donor.objects.create(user=user, documentType="cuentanos de tí",documentId="" , legalNature="")
        
    
#         return HttpResponse('Hello, World!')
        
