from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import *
from .functions import *
from datetime import date
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request,"hoteladmin/index.html",{
            "user":request.user.username.capitalize() } )
    else:
        return HttpResponseRedirect(reverse('hoteladmin:login'))
    
def view_login(request):
    if(request.method=="POST"):
        errormessage="Incorrect crendetials or the account doesnt exist"
        passmismatch="Passwords don't match.Please enter again."
        Permdenied="Permission Denied"
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            if user.groups.filter(name='HotelAdmin').exists():
                login(request,user)
                #Redirect to index view 
                return HttpResponseRedirect(reverse('hoteladmin:index'))
            else:
                return render(request,"hoteladmin/login.html",{
                    "message":Permdenied
                })
        else:
           return  render(request,"hoteladmin/login.html",{
               "message":errormessage
           })
    return render(request,"hoteladmin/login.html")

    

def register(request):
    if request.method=="POST":
        usernameexists="Username already exists.Choose a new username"
        userexists="Account already exists.Please sign in to continue"
        passerror="The passwords don't match.Please enter again"
        resexists="The  Restaurant  already exists"
        reserror="Cant Register Restaurant"
        addresserr="Can't Add Address Try Again"
        resname=request.POST['resname']
        street=request.POST['street']
        city=request.POST['city']
        pincode=request.POST['pincode']
        email=request.POST['email']
        seating_capacity=request.POST['seating_capacity']
        date=request.POST['date']
        open_time=request.POST['opening_time']
        close_time=request.POST['closing_time']
        cuisine=request.POST['cuisine']
        payment=request.POST['payment']
        takeaway=request.POST['takeaway']
        username=request.POST['user_name']
        password=request.POST['password']
        password1=request.POST['password1']
        addr=address.objects.create(street=street,city=city,pincode=pincode)
        no=get_number(Global)
        rest_id="DEF"+str(no)
        
        if addr is  None:
            return render(request,"hoteladmin/register.html",{
                "message":addresserr
            })
        if password!=password1:
            return render(request,"hoteladmin/register.html",{
                "message":passerror
            })
        allusers=User.objects.all()
        for user in allusers:
            if(user.username==username):
                if(user.email==email):
                    return render(request,"hoteladmin/register.html",{
                        "message":userexists
                    })
                
                return render(request,"hoteladmin/register.html",{
                    "message":usernameexists
                })
        user=User.objects.create_user(username=username,password=password,email=email)
       
        if user is not None:
            restaurant=Restaurant.objects.create(name=resname,address=addr,seating_capacity=seating_capacity,takeaway=takeaway,payment=payment,user=user,open_time=open_time,close_time=close_time,cuisine=cuisine,rest_id=rest_id)
            if restaurant is None:
                resall=Restaurant.objects.all()
                if restaurant in resall:
                    return render(request,"hoteladmin/register.html",{
                        "message":resexists
                    })
                else:
                    return render(request,"hoteladmin/register.html",{
                        "message":reserror
                    }) 
            else:
                group=Group.objects.get(name='HotelAdmin')
                group.user_set.add(user)
                group.save()
                return HttpResponseRedirect(reverse('hoteladmin:login'))
        else:
            return render(request,"hoteladmin/register.html",{
                        "message":"User Cant be created"
                    }) 
           
    return render(request,"hoteladmin/register.html")

def view_orders(request):
    user=request.user
    restaurant=user.restaurant
    orders=restaurant.orders.all()
    
    return render(request,"hoteladmin/orders.html",{
        "orders":orders,
    })
def expand_order(request,order_no):
    order=Order.objects.get(order_no=order_no)
    return render(request,"hoteladmin/expandorder.html",{
        "order":order
    })

