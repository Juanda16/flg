from django.shortcuts import render
from app.models import Donor
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from django.views import View
from django.http import QueryDict
#from django.views.decorators.csrf import csrf_exempt


# Views here.

def index(request):
   return render(request, 'app/index.html', {})

 
class DonorView(View):
   def get(self, request, *args, **kwargs):
      
      return HttpResponse('Esto es un get correcto!')

   
   def post(self, request, *args, **kwargs):
      userName= request.POST["userName"]
      email = request.POST["email"]
      password = request.POST["password"]
      user = User.objects.create_user(userName, email, password)
      Donor.objects.create(user=user,documentType=request.POST["documentType"], documentId=request.POST["documentId"])
      
      

      return HttpResponse(user)

   def put(self,request,*args,**kwargs):
      put = QueryDict(request.body)
      
      try:
         _userid = kwargs['pk']
         user = User.objects.get(id=_userid)
         user.userName = put.get('userName')
         user.email = put.get('email')
         user.password = put.get('password')
         user.save()
         donor = Donor.objects.get(user_id=_userid)
         donor.documentType = put.get('documentType')
         donor.documentId = put.get('documentId')
         donor.save()

         return HttpResponse(user)

      except User.DoesNotExist:

         return HttpResponse("user doesn´t exist")
      
      

      
    
    


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
        
