from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group

# Create your views here.

def index(request):
    return render(request,"hoteladmin/index.html")
def view_login(request):
    return render(request,"hoteladmin/login.html")

def register(request):
    return render(request,"hoteladmin/register.html")
