from django.urls import path
from . import views
app_name="hoteladmin"
urlpatterns = [
    path("/",views.index,name="index"),
    path("/login",views.view_login,name="login")
]

