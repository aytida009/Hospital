from django.db import models
from datetime import datetime, date
from django.utils import timezone

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=50,verbose_name="Your Name ")
    email = models.EmailField(max_length=75,verbose_name="Your Email ")
    mobile = models.CharField(max_length=15,verbose_name="Your Mobile ")
    selectservice = models.CharField(max_length=15,verbose_name="Your Service")
    appointmentdate = models.DateField(auto_now_add=True,blank=True,null=True)
    appointmenttime = models.TimeField(auto_now_add=True,auto_now=False,blank=True)
    specialrequest = models.CharField(max_length=50,verbose_name="Youe Special Request")
    
    class Meta:
        db_table= "Booking"



class contactus(models.Model):
    name = models.CharField(max_length=50,verbose_name="Your Name ")
    email = models.EmailField(max_length=75,verbose_name="Your Email ")
    subject = models.TextField(max_length=600,verbose_name="Your subject ")
    message = models.TextField(max_length=600,verbose_name="message ")
    
    class Meta:
        db_table= "contactus"
        

        
class MyServices(models.Model):
    title = models.CharField(max_length=50)
    short_desc = models.TextField() 
    price = models.IntegerField()   
    
    class Meta:
        db_table= "My Services"
    
