from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from django.core.urlresolvers import reverse_lazy
from models import Donor
#from models import * 

#if request.method == 'GET':
        user = User.objects.GET(id)
        Donor.objects.GET(user)
        return HttpResponse("variables")
    


    
