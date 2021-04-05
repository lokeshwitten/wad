from hoteladmin.models import *

def get_code(Restaurant):
    city=Restaurant.address.city
    street=Restaurant.address.street
    pincode=Restaurant.address.pincode
    name=Restaurant.name
    id=Restaurant.rest_id
    code= name+'-'+street+'-'+city+'-'+str(pincode)+'-'+id
    return code
def decode(code):
    decode=code[::-1]
    i=0
    while(code[i]!='-'):
        i+=1
    i=+1
    return code[:i]
    
