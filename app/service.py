#from django.views.generic import ListView
#from django.views.generic.detail import DetailView
#from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
#from django.core.urlresolvers import reverse_lazy

from models import Donor
#from models import DonorView
from models import * 
from django.contrib.auth.models import User
from django.http import QueryDict

def gettingUser(id)
    user = User.objects.get(id=id)
    donor=Donor.objects.get(user_id=user.id)
    return donor

def postingUser(userName,email,password,documentType,documentId)
    userName= request.POST["userName"]
    email = request.POST["email"]
    password = request.POST["password"]
    user = User.objects.create_user(userName, email, password)
    Donor.objects.create(user=user,documentType=request.POST["documentType"], documentId=request.POST["documentId"])
    return donor

def puttingUser(userName,email,password,documentType,documentId)
    put = QueryDict(request.body)
        
    try:
        _userid = kwargs['pk']
        user = User.objects.get(id=_userid)
        user.username = put.get('username')
        user.first_name = put.get('first_name')
        user.last_name = put.get('last_name')
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

def deletingUser(Id)
    request.DELETE = QueryDict(request.body)
    entity_id=request.DELETE.get('entity_id')    
    if not entity_id:
        return self.render_json_response({'state':False, 'error':'entity_id is required'},
        status=400
    group=GroupPermission.objects.get_by_id(entity_id)
    group.delete()
    return self.render_json_response({'state':True},

    