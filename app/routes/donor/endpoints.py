# todo lo relacionado con los endpoints del donante 
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from app.views import userView

urlpatterns = [
    path("", userView.index, name="index"),
    path('index', userView.index, name='index_view'),    
    path('<int:pk>',userView.DonorView.as_view(), name='donor_view_detail'), 
    path("login", userView.login_view, name="login"),
    path("logout", userView.logout_view, name="logout")
]