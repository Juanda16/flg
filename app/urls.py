from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index_view'),
    path('donor', views.DonorView.as_view(), name='donor_view'),
        
]