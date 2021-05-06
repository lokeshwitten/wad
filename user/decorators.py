from hoteladmin.models import *
import qrcode
import cv2

def get_code(Restaurant):
    city=Restaurant.address.city
    street=Restaurant.address.street
    pincode=Restaurant.address.pincode
    name=Restaurant.name
    id=Restaurant.rest_id
    code= name+'-'+street+'-'+city+'-'+str(pincode)+'-'+id
    return code

#Decoding the string and converting it into a dictionary
def decode(string):
    resdict={}
    con=''
    for i in range(len(string)):
        if (string[i]=='+' or string[i]=='-'):
            if(string[i]=='+'):
                if int(con) in resdict:
                    resdict[int(con)]+=1
                    con=''
                else:
                    resdict[int(con)]=1
                    con=''
            if(string[i]=='-'):
                resdict[int(con)]-=1
                con=''
        else:
            if(string[i]=='q'):
                i+=1
            else:
                con+=string[i]
    return resdict



def readqr():
# initalize the cam
    cap = cv2.VideoCapture(0)
    #initialize the cv2 QRCode detector
    detector = cv2.QRCodeDetector()
    while True:
        _, img = cap.read()
        # detect and decode
        data, bbox, _ = detector.detectAndDecode(img)
        # check if there is a QRCode in the image
        if bbox is not None:
            # display the image with lines
            for i in range(len(bbox)):
                # draw all lines
                cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)
            if data:
                print("[+] QR Code detected, data:", data)
                break
        # display the result
            cv2.imshow("img", img)    
        if cv2.waitKey(1) == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
    return data
    
#Checking if the user has an existing order
def order_exists(user):
    orders=user.orders.all()
    latest_order=orders.last()
    if latest_order is None:
        return False
    if(latest_order.bill_status=='PD'):
        return True
    else:
        return False

def common(a,b):
    common=[]
    for i in a.keys():
        for j in b.keys():
            if(i==j):
                common.append(i)
    return common
#Merging Orderdata
def merge_dict(a,b):
    #Find the common keys
    ret={}
    com=common(a,b)
    for key in com:
        ret[key]=a[key]+b[key]
    
    #Deleting the common keys in the dicts
    for key in com:
        del a[key]
        del b[key]
    #Populate the merged dictionary with values that are not common
    for key in a.keys():
        ret[key]=a[key]
    for key in b.keys():
        ret[key]=b[key]

    return ret
#Get Price of the order from the dictionary
def get_price(dict):
    price=0
    for key in dict.keys():
        quantity=dict[key]
        dish=Dish.objects.get(pk=key)
        price+=int(dish.price*quantity)
    return price

#Functions for reservations

#Return the tables available 
def tables_avail(Restaurant):
    avail_capacity=Restaurant.capacity
    reservations=Restaurant.reservations.all()
    if reservations is None:
        return avail_capacity
    else: 
        for reservation in reservations:
            avail_capacity-=reservation.tables
        return avail_capacity
def set_tableno(Reservation):
    restaurant=Reservation.restaurant
    reservations=restaurant.reservations.all()
    list=[]
    populate(list,restaurant.capacity)
    #If this is the first reservation
    if(restaurant.reservations.count()==1):
        table_no=extract_min(list,int(Reservation.tables))
        table_no= [str(element) for element in table_no]
        string=",".join(table_no)
        string+=','
        Reservation.table_no=string
        Reservation.save()
    else:
        avail_tables=[]
        string=''
        for reservation in reservations:
            string+=reservation.table_no
        string=string[:len(string)-1]
        tables_occupied=string.split(",")
        tables_occupied=[int(element) for element in tables_occupied ]
        tables_avail=Diff(tables_occupied,list)
        table_no=extract_min(tables_avail,int(Reservation.tables))
        table_no= [str(element) for element in table_no]
        table_no=",".join(table_no)
        table_no+=','
        Reservation.table_no=table_no
        Reservation.save()

def populate(list,no):
    for i in range(1,no+1):
        list.append(i)
def Diff(li1, li2):
    li3=li2
    for i in li1:
        li3.remove(i)
    return li3

def extract_min(l,no):
    list=l
    ret=[]
    for i in range(0,no):
        a=min(list)
        ret.append(a)
        list.remove(a)
    return ret

        
        