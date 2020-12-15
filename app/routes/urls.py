from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings

#admin.autodiscover()
from django.views.generic.base import TemplateView
from app.views import userView

urlpatterns = [
    #api version 1
    #path("", userView.index, name="index"),
    #path('index', userView.index, name='index_view'),
    path('api/v1/donor/',include('app.routes.donor.endpoints')),
    path('api/v1/donation', include('app.routes.donation.endpoints'))
    #path('api/v1/certificate', userView.DonorsView.as_view(), name='donor_view'),
    url(r'^getData/', userView.get_data),
    #url(r'^.*', TemplateView.as_view(template_name="home.html"), name="home")
 ]
