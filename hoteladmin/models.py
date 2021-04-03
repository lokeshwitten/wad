from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class address(models.Model):
    street=models.CharField (max_length=50)
    city=models.CharField( max_length=50)
    pincode=models.IntegerField()

    def __str__(self):
        return f" {self.street} \n{self.city} \n{self.pincode} "

class Dish(models.Model):
    NORTH_INDIAN='NIN'
    ITALIAN='IT'
    CHINESE='CHI'
    SOUTH_INDIAN='SIN'
    KOREAN='KR'
    SIDE='SD'
    DESSERT='DES'
    BURGER='BUR'
    BEVERAGES='BEV'
    DEFAULT='DEF'
    SOUP='SOU'
    SALAD='SAL'
    CATEGORY=[(NORTH_INDIAN,'North Indian'),(ITALIAN,"Italian"),(CHINESE,'Chinese'),
    (SOUTH_INDIAN,'South Indian'),(KOREAN,'Korean'),(SIDE,'Side'),(DESSERT,'Dessert'),
    (BURGER,'Burger'),(BEVERAGES,'Beverages'),(SOUP,'Soup'),(SALAD,"Salad")]
    TIME=[('BR','BreakFast'),('LN','Lunch'),('DI','Dinner')]
    name=models.CharField( max_length=50)
    image=models.ImageField(upload_to='.',blank=True)
    avail=models.BooleanField(default=True)
    served_at=models.CharField(max_length=2,choices=TIME,blank=True)

    price=models.IntegerField()
    category=models.CharField( max_length=4,choices=CATEGORY,default=DEFAULT)

    
    def __str__(self):
        return f"{self.name} - {self.price}"
class Order(models.Model):
    PENDING='PD'
    CONFIRM='CON'
    PAID='PD'
    ORDER_STATUS=[(PENDING,'Pending'),(CONFIRM,'Confirm')]
    BILL_STATUS=[(PENDING,'Pending'),(PAID,'Paid')]
    order_no=models.CharField(max_length=10,primary_key=True)
    items=models.ManyToManyField(Dish,related_name='+')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    order_status=models.CharField(max_length=3,choices=ORDER_STATUS,default=PENDING)
    bill_status=models.CharField(max_length=3,choices=BILL_STATUS,default=PENDING)
    restaurant=models.OneToOneField('Restaurant',related_name='+',on_delete=models.CASCADE,null=True)
    date=models.DateField(blank=True,null=True)
    time=models.TimeField(blank=True,null=True)
    avg_time=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.order_no} "



class Restaurant(models.Model):
    avail_payment=[('GPAY','Google Pay'),('UPI','UPI PhonePe')]
    MULTI='MC'
    Cuisine=[(MULTI,'MultiCuisine Restaurant'),('VEG','Pure Veg')]
    OPEN='OP'
    CLOSED='CL'
    STATUS=[(OPEN,'Open'),(CLOSED,'Closed')]
    name=models.CharField( max_length=50)
    address=models.ForeignKey( address, on_delete=models.CASCADE,related_name="restaraunt")
    dishes=models.ManyToManyField(Dish,blank=True,related_name='restaraunt')
    capacity=models.IntegerField(default=20)
    takeaway=models.BooleanField(blank=True,default=False)
    payment=models.CharField(max_length=4,choices=avail_payment,default='Cash')
    orders=models.ManyToManyField(Order,blank=True,related_name='+')
    combos=models.ManyToManyField(Dish,blank=True,related_name='+')
    open_time=models.TimeField(blank=True,null=True)
    date=models.DateField(null=True)
    close_time=models.TimeField(blank=True,null=True)
    cuisine=models.CharField(max_length=4,choices=Cuisine,default=MULTI)
    status=models.CharField(max_length=3,choices=STATUS,default=OPEN)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='restaurant',null=True)
    rest_id=models.CharField(max_length=10,default='DEF001')

    class Meta:
        constraints=[
            models.UniqueConstraint(fields=['rest_id'],name='rest_id_constraint')
        ]
    def __str__(self):
        return f"{self.name} {self.cuisine} Restaraunt"


class Reservations(models.Model):
    PENDING='PD'
    CONFIRM='CON'
    STATUS=[(PENDING,'Pending'),(CONFIRM,'Confirm')]
    conf_code=models.CharField(max_length=10)
    cust_name=models.CharField(max_length =25)
    date=models.DateField(null=True)
    status=models.CharField(max_length=4)

    def __str__(self):
        return f"{self.conf_code} {self.cust_name}"
class Global(models.Model):
    order_no=models.IntegerField(default=0)
    cnf_no=models.IntegerField(default=0)
