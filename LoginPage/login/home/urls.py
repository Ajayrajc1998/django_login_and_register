from django.contrib import admin
from django.urls import path
from .views import home,register,login_user,logout_user,contact,faculty,Our_services,Book,adminpanel,DeleteUser,Useredit,SearchName,adminregister,confirmation

urlpatterns = [
    path('',login_user,name="login_user"),
    path('home/', home,name='home'),
    path('register/',register,name='register'),
    path('logout_user/',logout_user,name="logout_user"),
    path('faculty/',faculty,name="faculty"),
    path('contact',contact,name="contact"),
    path('services',Our_services,name='services'),
    path('Bookservice',Book,name='book'),
    path('adminpanel',adminpanel,name='adminpanel'),
    path('DeleteUser/<int:id>/',DeleteUser,name='DeleteUser'),
    path('useredit/ <int:id>/',Useredit,name='useredit'),
    path('search/',SearchName,name='search'),
    path('confirmation/',confirmation,name='confirmation'),
    path('adminregister/',adminregister,name='adminregister')

] 
