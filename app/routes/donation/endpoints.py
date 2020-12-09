#Todo relacionado con los endpoints de la donación 
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from app.views import userView

urlpatterns = [
    path("", donationView.index, name="index"),
    path('/index', donationsView.index, name='index_view'),    
    path('/<int:pk>',donationView.DonorView.as_view(), name='donor_view_detail'), 
]