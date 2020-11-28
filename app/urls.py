from django.urls import path
from . import views


urlpatterns = [
    #api version 1
    #path('index', views.index, name='index_view'),
    path('api/v1/donors', views.DonorsView.as_view(), name='donor_view'),# general donor - POST, GET methods implemented
    path('api/v1/donor/<int:pk>', views.DonorView.as_view(), name='donor_view_detail'),   #GET,PUT,DEL methods implemented
]