<<<<<<< HEAD
#from django.views.generic import ListView
#from django.views.generic.detail import DetailView
#from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
#from django.core.urlresolvers import reverse_lazy

=======
>>>>>>> 1fb8fb92c5b48b47d408e0c487b1970b0df17869
from app.models import Donor
from django.contrib.auth.models import User
from django.http import QueryDict

# business logic

def gettingUser(id):
    user = User.objects.get(id=id)
    donor=Donor.objects.get(user_id=user.id)
    return donor

def postingUser(request):
    userName= request.POST["userName"]
    email = request.POST["email"]
    password = request.POST["password"]
    user = User.objects.create_user(userName, email, password)
    donor = Donor.objects.create(user=user,documentType=request.POST["documentType"], documentId=request.POST["documentId"])
    return donor

def puttingUser(request,id):
    put = QueryDict(request.body)
        
    try:
        userid = id
        user = User.objects.get(id=userid)
        user.first_name = put.get('first_name')
        user.last_name = put.get('last_name')
        user.email = put.get('email')
        user.password = put.get('password')
        user.save()
        donor = Donor.objects.get(user_id=userid)
        donor.documentType = put.get('documentType')
        donor.documentId = put.get('documentId')
        donor.save()

        return donor

    except User.DoesNotExist:

        return "user doesn´t exist"

def deletingUser(request,Id):
    donor = Donor.objects.get(user_id=Id)
    donor.delete()
    user = User.objects.get(id=Id)
    user.delete()    
    return ()
<<<<<<< HEAD

    
=======
>>>>>>> 1fb8fb92c5b48b47d408e0c487b1970b0df17869
