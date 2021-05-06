from django.urls import path
from . import views
app_name='user'
from django.conf import settings

from django.conf.urls.static import static

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
   
    path('cart',views.cart,name='cart'),
    path('/orderconf',views.order_conf,name='orderconf'),
    path('/ordersuccess',views.place_order,name='ordersuccess'),
    path('ajax/validate_username',views.validate_username,name='validate_username')

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
