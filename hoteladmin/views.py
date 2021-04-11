from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/hoteladmin/login')
def index(request):
    return render(request,"hoteladmin/index.html")
def view_login(request):
    return render(request,"hoteladmin/login.html")