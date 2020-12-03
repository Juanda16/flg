from django.urls import path
from app.views.userView import DonorsView,DonorView

urlpatterns = [
    #api version 1
    path("", userView.index, name="index"),
    path('index', userView.index, name='index_view'),
    path('api/v1/donor', userView.DonorsView.as_view(), name='donor_view'),# general donor - POST, GET methods implemented
    path('api/v1/donation', userView.DonorsView.as_view(), name='donor_view'),
    path('api/v1/certificate', userView.DonorsView.as_view(), name='donor_view'),

    path()
    """ path('api/v1/donor/<int:pk>', userView.DonorView.as_view(), name='donor_view_detail'), 
    path('api/v1/donors', userView.DonorsView.as_view(), name='donor_view'),# general donor - POST, GET methods implemented
    path('api/v1/donor/<int:pk>', userView.DonorView.as_view(), name='donor_view_detail'),   #GET,PUT,DEL methods implemented
    path("login", userView.login_view, name="login"),
    path("logout", userView.logout_view, name="logout"),
    path("profile", userView.profile_view, name="profile"),
    #path('social-auth', include('social_django.urls', namespace="social")),
    path("register",userView.register_view, name="register"),
    path("new_user",userView.new_user, name="new_user"),
    path("new_profile",userView.new_profile, name="new_profile"),
    path("edit_user",userView  .edit_user, name="edit_user"), """



]


