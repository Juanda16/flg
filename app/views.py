from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from django.core.urlresolvers import reverse_lazy
from models import Donor
from models import DonorView
from models import * 

class DonorView(View):
        def get(self, request,*args,**kwargs):
                _userid=kwargs['pk']
                user = User.objects.get(id=_userid)
                Donor.objects.get(user_id=user.id)
                return HttpResponse("Diana, esta bien")
    

    
