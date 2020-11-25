from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    #path('index', views.index, name='index_view'),
    path('api/v1/donors', views.DonorView.as_view(), name='donor_view'),
    path('api/v1/donors/<int:pk>', views.DonorView.as_view(), name='donor_view_detail'),   

=======
    path('index', views.index, name='index_view'),
    path('donors', views.DonorView.as_view(), name='donor_view'),
    path('donors/<int:pk>', views.DonorView.as_view(), name='donor_view_detail'),
        
>>>>>>> db0b87fec8308048d0247d3eedb31541a1628ca7
]