#Todo relacionado con los endpoints de la donación 
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from app.views import donationView

urlpatterns = [
    #path("", DonationView.index, name="index"),
    #path('index', DonationsView.index, name='index_view'),  
    path('',donationView.DonationsView.as_view(), name='donation_view_general'),  
    path('<int:pk>',donationView.DonationView.as_view(), name='donation_view_detail'), 
]