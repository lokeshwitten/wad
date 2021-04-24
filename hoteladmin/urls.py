from django.urls import path
from . import views
app_name="hoteladmin"
urlpatterns = [
    path("/",views.index,name="index"),
    path("/login",views.view_login,name="login"),
    path("/register",views.register,name='register'),
    path("/orders",views.view_orders,name='orders'),
    path("/orders/<str:order_no>",views.expand_order,name='expandorder')
]

