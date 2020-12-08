from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

import datetime
import json
import requests
import uuid

from .models import *
# Create your views here.

def home(request):
    return render(request, 'product.html')

def exchanged_rate():
    url = "https://blockchain.info/tobtc?"
    params = {
        "currency":"USD",
        "value":0.02,
    }
    r = requests.get(url, params= params)
    print(r.json())
    return r.json()

def create_payment(request):
    amount = 0.02 # In USD

    url = 'https://www.blockonomics.co/api/new_address'
    headers = {'Authorization': "Bearer " + settings.API_KEY}
    r = requests.post(url, headers=headers)
    print(r.json())
    if r.status_code == 200:
        address = r.json()['address']
        bits = exchanged_rate()
        order_id = uuid.uuid1()
        data = {
            'order_id':order_id,
            'bits':bits,
            'value':0.02,
            'addr': address,
        }
        Invoice.objects.create(order_id=order_id,
        address=address,value=bits)
        return render(request,"invoice.html", context=data)
    else:
        print(r.status_code, r.text)
        return HttpResponse("Some Error, Try Again!")
    
def receive_payment(request):
    print(request.method)
    if (request.method != 'GET'):
        return 
    
    txid  = request.GET.get('txid')
    value = request.GET.get('value')
    status = request.GET.get('status')
    addr = request.GET.get('addr')

    invoice = Invoice.objects.get(address = addr)
    invoice.status = int(status)
    invoice.received = float(value)
    invoice.txid = txid
    invoice.save()
    return HttpResponse(200)

def check_payment(request):
    if (request.method != 'GET'):
        return 
    address = request.GET.get('addr')
    invoice_obj = Invoice.objects.get(address = address)
    data = {
        'status':invoice_obj.status,
    }
    print(address)
    return HttpResponse(json.dumps(data), content_type='application/json')