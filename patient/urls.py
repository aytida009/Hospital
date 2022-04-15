
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index),
    path('index', views.index, name='index'),
    path('about',views.about,name='about'),
    path('booking',views.booking,name='booking'),
    path('contact',views.contact,name='contact'),
    path('login',views.login,name='login'),
    path('service',views.service,name='service'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('signuppage',views.signuppage,name='signuppage'),
    path('signinpage',views.signinpage,name='signinpage'),
    path('logout',views.logout,name='logout'),
    path('contactpage',views.contactpage,name='contactpage'),
    path('userhome',views.userhome,name='userhome'),
    path('Appointment',views.Appointment,name='Appointment'),
    
  
]