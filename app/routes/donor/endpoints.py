# todo lo relacionado con los endpoints del donante 
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from app.views import userView

urlpatterns = [
    path("", userView.DonorsView.as_view(), name="donor_View_Post"),
    path('<int:pk>',userView.DonorView.as_view(), name='donor_view_detail'), 
    #path('<int:pk>',userView.donor_detail, name='donor_detail'),
<<<<<<< HEAD
    path("login", userView.LoginUserView.as_view(), name="login"),
    path("logout", userView.logout_view, name="logout"),
=======
    #path("login", userView.views.LoginUserView.as_view(), name="login"),
    #path("logout", userView.logout_view, name="logout"),
>>>>>>> a7313b46315ccb4ed8096b7912d0917a2d41018e
    
]