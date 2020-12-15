# todo lo relacionado con los endpoints del donante 
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from app.views import userView

urlpatterns = [
    path("", userView.DonorsView.as_view(), name="donor_View_Post"),
    path('<int:pk>',userView.DonorView.as_view(), name='donor_view_detail'), 
    #path('<int:pk>',userView.donor_detail, name='donor_detail'),
    path("login", userView.LoginUserView.as_view(), name="login"),
    path("logout", userView.logout_view, name="logout"),
    
]