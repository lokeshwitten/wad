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
    
def merge_dict(a,b):
    #Find the common keys
    common=[]
    for i in a.keys():
        for j in b.keys():
            if(i==j):
                common.append(i)
    return common


