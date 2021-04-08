from django.urls import path
from . import views
app_name='user'

urlpatterns = [
    path("/",views.index,name="index"),
    path("/login",views.view_login,name="login"),
    path("/signup",views.signup,name="signup"),
    path("/contact",views.contact,name="contact"),
    path("/test",views.test,name="test"),
    path("/restaurant/<str:rest_id>",views.view_restaurant,name='view_restaurant'),
    path("/booking/",views.booking,name='booking'),
    path("/booking/confirmreservation",views.confirm_res,name='confirmres'),
    path("/qrcode",views.qrcode,name='qrcode'),
    path("/logout",views.logout_view,name='logout'),
    path("test1",views.test1,name='test1'),
    path('cart',views.cart,name='cart')

]
