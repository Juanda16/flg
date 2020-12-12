# todo lo relacionado con los endpoints del donante 
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from app.views import userView

urlpatterns = [
    path("", userView.DonorsView.as_view(), name="index"),
    path('<int:pk>',userView.DonorView.as_view(), name='donor_view_detail'), 
    path("login", userView.login_view, name="login"),
    path("logout", userView.logout_view, name="logout"),
    
]