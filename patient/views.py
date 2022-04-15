from django.shortcuts import  get_object_or_404,render, HttpResponseRedirect

from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import contactus
from .models import Booking

from django.contrib import auth
from .models import  MyServices


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request,'about.html')

def booking(request):
    # if request.method=="POST":
    #     unm=request.POST['username']
    #     pwd=request.POST['password']
    #     user=auth.authenticate(username=unm,password=pwd)
    #     if user is not None:
    #          auth.login(request,user)
    #          return render(request,'booking.html')
    #     else:
    #          return render(request,'signup.html')
    # else:
    #     return render(request,'signup.html')
    
    return render(request,'booking.html')

def contact(request):
    return render(request,'contact.html')

def login(request):
    return render(request,'login.html')

def service(request):
    return render(request,'service.html')

def signup(request):
    return render(request,'signup.html')

def signin(request):
    return render(request,'signin.html')

def signuppage(request):
    if request.method=="POST":
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        email=request.POST['email']
        unm=request.POST['username']
        pwd=request.POST['password']
        try:
            user=User.objects.get(usename=unm)
            return  render(request,'signup.html')
        except:
            user=User.objects.create_user(first_name=fname,last_name=lname,email=email,username=unm,password=pwd)
            user.save()
            return render(request,'signin.html')
    else:
        return  render(request,'signup.html')
    

def signinpage(request):
    if request.method=="POST":
        unm=request.POST['username']
        pwd=request.POST['password']
        user=auth.authenticate(username=unm,password=pwd)
        if user is not None:
             auth.login(request,user)
             return render(request,'index.html')
        else:
             return render(request,'signin.html')
    else:
        return render(request,'signin.html')
    
def logout(request):
    auth.logout(request)
    return render(request,'index.html')

def contactpage(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        # # send an email
        # send_mail(
        #     name, # name
        #     email, # from email
        #     subject, # subject 
        #     message, # message
        #     ['aditya.it1902@mitindore.co.in'],# To Email
        # )
       
        Contact = contactus(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )        
        Contact.save({'name':name,'email':email,'subject':subject,'message':message})
        return render(request,'contact.html',{'name':name})
        # return redirect(request,'contact.html',{'message_name':message_name})
    return render(request,'contact.html',)
        
def Appointment(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        selectservice = request.POST['selectservice']
        appointmentdate = request.POST['appointmentdate']
        appointmenttime = request.POST['appointmenttime']
        specialrequest = request.POST['specialrequest']
        
        Fixed=Booking(
            name=name,
            email=email,
            mobile=mobile,
            selectservice=selectservice,
            appointmentdate=appointmentdate,
            appointmenttime=appointmenttime,
            specialrequest=specialrequest,
            )
        Fixed.save({'name':name,'email': email,'mobile': mobile,'selectservice': selectservice,'appointmentdate' : appointmentdate,'appointmenttime' : appointmenttime,'specialrequest' :specialrequest})
        return render(request,'userhome.html',{
            'name': name,
            'email': email,
            'mobile': mobile,
            'selectservice': selectservice,
            'appointmentdate' : appointmentdate,
            'appointmenttime' : appointmenttime,
            'specialrequest' :  specialrequest,
            })
    else:
        return render(request,'index.html',)
    
def userhome(request):
    return render(request,'userhome.html')

def myservices(request):
     if request.method == "POST":
      tittle = request.GET['tittle']
      short_desc = request.GET['short_desc']
      price = request.GET['price']
     
     Fixed = MyServices(
         tittle=tittle,
         short_desc=short_desc,
         price=price,
     )
     Fixed=save({'tittle':tittle,'short_desc':short_desc,'price':price})
     return render(request,'index.html',{
         'tittle':tittle,
         'short_desc':short_desc,
         'price':price,
     })
     

    
    

     
     