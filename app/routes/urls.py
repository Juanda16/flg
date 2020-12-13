from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings

#admin.autodiscover()

urlpatterns = [
    #api version 1
    #path("", userView.index, name="index"),
    #path('index', userView.index, name='index_view'),
    path('v1/donor',include('app.routes.donor.endpoints')),
    path('v1/donation/',include('app.routes.donation.endpoints')),
    #path('api/v1/certificate', userView.DonorsView.as_view(), name='donor_view'),
 ]
