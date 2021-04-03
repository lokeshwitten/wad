from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http  import HttpResponseRedirect,HttpResponse
from django.urls import reverse
# Create your views here.
from hoteladmin.models import *

def index(request):
    request.session.set_expiry(0)
    if request.user.is_authenticated:
        username=request.user.username.capitalize()
        return render(request,"user/index.html",{
            "username":username
        })
    else: #Ask the user to login
        return HttpResponseRedirect(reverse('user:login'))

def signup(request):
    if(request.method=="POST"):
        #Error messages
        usernameexists="Username already exists.Choose a new username"
        userexists="Account already exists.Please sign in to continue"
        passerror="The passwords don't match.Please enter again"
        #POST data
        username=request.POST['username']
        password=request.POST.get('password')
        passverify=request.POST.get('password1')
        email=request.POST.get('email')

        #Checking whether the entered two passwords match
        if password != passverify:
            return render(request,"user/signup.html",{
                "message":passerror
            })
        
        #Checking if the username or the user already exists
        allusers=User.objects.all()
        for user in allusers:
            if(user.username==username):
                if(user.email==email):
                    return render(request,"user/signup.html",{
                        "message":userexists
                    })
                
                return render(request,"user/signup.html",{
                    "message":usernameexists
                })
        user=User.objects.create_user(username=username,password=password,email=email)
        user.save()
        userauth=authenticate(username=username,password=password)
        if userauth:
            #Redirect to login view
            return HttpResponseRedirect(reverse('user:login'))
        else:
            return HttpResponse(request,"Cant create user")
    return render(request,"user/signup.html")
def view_login(request):
    if(request.method=="POST"):
        errormessage="Incorrect crendetials or the account doesnt exist"
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:    
            login(request,user)
            #Redirect to index view
            return HttpResponseRedirect(reverse('user:index'))

        else:
           return  render(request,"user/login.html",{
               "message":errormessage
           })
    return render(request,"user/login.html")
def contact(request):
    return render(request,"user/contact.html")

def booking(request):
    if request.method=="POST":
        date=request.POST["date"]
        return render(request,"user/test.html",{
            "date":date
        })
    return render(request,"user/booking.html")
def test(request):
    ord1=Order.objects.get(pk='ORD001')
    return render(request,"user/test.html",{
        'ord1':ord1
    })
    
def view_restaurant(request,rest):
    pass