from django.urls import path
from . import views
app_name='user'

urlpatterns = [
    path("",views.index,name="index"),
    path("login",views.view_login,name="login"),
    path("signup",views.signup,name="signup"),
    path("contact",views.contact,name="contact"),
    path("booking",views.booking,name="booking"),
    path("test",views.test,name="test"),
    #path("restaurant/<string:rest>",views.view_restaurant,name='view_restaurant')

]
