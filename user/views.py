from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.http  import HttpResponseRedirect,HttpResponse,JsonResponse
from django.urls import reverse
# Create your views here.
from hoteladmin.models import *
from .decorators import *
from django.contrib.auth.decorators import login_required
from datetime import date,time
from datetime import datetime
from wad.settings import BASE_DIR


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
        passmismatch="Passwords don't match.Please enter again."
        username=request.POST['username']
        password=request.POST['password']
       
        user=authenticate(request,username=username,password=password)
        if user is not None:    
            login(request,user)
            #Redirect to index view
            
            return HttpResponseRedirect(reverse('user:index',))

        else:
           return  render(request,"user/login.html",{
               "message":errormessage
           })
    return render(request,"user/login.html")
def contact(request):
    return render(request,"user/contact.html")

def booking(request,):
    if request.method=="POST":
        request.session['rests']=request.POST['rest']
        rest_code=request.session['rests']
        restaurant=Restaurant.objects.get(rest_id=rest_code)
        capacity=tables_avail(restaurant)
        return render(request,"user/booking.html",{
            "no":capacity
        })
    return HttpResponseRedirect(reverse('user:test'))
def test(request):
    return render(request,"user/test.html",{
        "restaurants":Restaurant.objects.all()
    })
def confirm_res(request):
    if request.method=="POST":
        tables=request.POST['no'] #No of the tables
        name=request.POST['name'] #Name of the customer
        date=request.POST['date'] #date of reservation
        time=request.POST['time'] #Time
        rest_code=request.session['rests']
        restaurant=Restaurant.objects.get(rest_id=rest_code)
        glob=Global.objects.get(pk=1)
        cnf_code='CNF'+str(glob.cnf_no)
       
        rest_id=request.session['rests']
        reservation=Reservations.objects.create(conf_code=cnf_code,user=request.user,cust_name=name,date=date,
        tables=tables,time=time,restaurant=restaurant)
        if reservation is not None:
            glob.cnf_no +=1
            glob.save()
            set_tableno(reservation)
            reservation.save()
            return render(request,"user/resconfirm.html",{
                "reservation":reservation
            })
        else:
            return HttpResponse('Reservation cant be made ')
    
    return HttpResponseRedirect(reverse('user:test'))   
    
@login_required(redirect_field_name='/usertest1',login_url='/user/login')
def view_restaurant(request,rest_id):
    if request.method=="POST":
        orderdata=request.POST['orderdata']
        request.session['cart']=decode(orderdata) #First time the user orders
        return HttpResponseRedirect(reverse('user:orderconf'))
    restaurant=Restaurant.objects.get(rest_id=rest_id)
    request.session['rest']=rest_id
    return render(request,"user/menu.html",{
        "restaurant":restaurant,"dishes":restaurant.dishes.all()
    })
def qrcode(request):
    data=readqr()
    return HttpResponseRedirect(data)
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('user:login'))
#Order Confirmation page
def order_conf(request):
    orderdata=request.session['cart']
    items={}
    price=get_price(orderdata)
    for key in orderdata.keys():
        dish=Dish.objects.get(pk=key)
        quantity=orderdata[key]
        items[dish]=quantity
    return render(request,"user/orderconf.html",{
        "dishes":items,"price":price,
    })
        


def cart(request):
    orderdata=request.session['cart']
    items=[]
    for key in orderdata.keys():
        dish=Dish.objects.get(pk=key)
        quantity=orderdata[key]
        items.append(dish.name+ str(quantity)+ 'X'+ '-' +str(dish.price*quantity) )
    return render(request,"user/cart.html",{
        "items":items
    })
def place_order(request):
    if request.method=="POST":
        if(order_exists(request.user)):
            pass
        else:
            pass
#Testing Ajax
def validate_username(request):
    username=request.GET['username']
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)

    

 