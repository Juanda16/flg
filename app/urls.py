from django.urls import path
from . import views


urlpatterns = [
<<<<<<< HEAD
    #path('index', views.index, name='index_view'),
    path('api/v1/donors', views.DonorView.as_view(), name='donor_view'),
    path('api/v1/donors/<int:pk>', views.DonorView.as_view(), name='donor_view_detail'),   

=======
    #api version 1
    #path('index', views.index, name='index_view'),
    path('api/v1/donors', views.DonorsView.as_view(), name='donor_view'),# general donor - POST, GET methods implemented
    path('api/v1/donor/<int:pk>', views.DonorView.as_view(), name='donor_view_detail'),   #GET,PUT,DEL methods implemented
>>>>>>> 1fb8fb92c5b48b47d408e0c487b1970b0df17869
]