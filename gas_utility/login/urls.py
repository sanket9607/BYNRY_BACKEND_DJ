from django.urls import path
from . import views


urlpatterns = [
    path('',views.authlogin,name='login'),
    path('registration/', views.registration, name='registration'),
    path('forget-password', views.forgetpassword, name='forgetpassword'),
    path('logout/', views.authlogout, name='logout'), ]


