from django.urls import path
from . import views

urlpatterns = [

    #path('index', views.index, name='index_view'),
    path('api/v1/donors', views.DonorView.as_view(), name='donor_view'),
    path('api/v1/donors/<int:pk>', views.DonorView.as_view(), name='donor_view_detail'),   

]