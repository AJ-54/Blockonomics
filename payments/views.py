from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings

import datetime
import json
import requests
import uuid
import os

from .models import *
# Create your views here.

def home(request):

    products = Product.objects.all()
    return render(request, 'product.html', context = {"products":products})

def exchanged_rate(amount):
    url = "https://blockchain.info/tobtc?"
    params = {
        "currency":"USD",
        "value":amount,
    }
    r = requests.get(url, params= params)
    print(r.json())
    return r.json()

def track_invoice(request, pk):
    invoice_id = pk
    invoice = Invoice.objects.get(id=invoice_id)
    data = {
            'order_id':invoice.order_id,
            'bits':invoice.value/1e8,
            'value':invoice.product.price,
            'addr': invoice.address,
            'status':Invoice.STATUS_CHOICES[invoice.status+1][1],
            'invoice_status': max(0,invoice.status),
        }
    if (invoice.received):
        data['paid'] =  invoice.received/1e8
        if (int(invoice.value) <= int(invoice.received)):
            data['path'] = invoice.product.product_image.url
    else:
        data['paid'] = 0  

    return render(request,'invoice.html',context=data)

def create_payment(request, pk):
    
    product_id = pk
    product = Product.objects.get(id=product_id)
    url = 'https://www.blockonomics.co/api/new_address'
    headers = {'Authorization': "Bearer " + settings.API_KEY}
    r = requests.post(url, headers=headers)
    print(r.json())
    if r.status_code == 200:
        address = r.json()['address']
        bits = exchanged_rate(product.price)
        order_id = uuid.uuid1()
        invoice = Invoice.objects.create(order_id=order_id,
                                address=address,value=bits*1e8, product=product)
        return HttpResponseRedirect(reverse('payments:track_payment', kwargs={'pk':invoice.id}))
    else:
        print(r.status_code, r.text)
        return HttpResponse("Some Error, Try Again!")
    
def receive_payment(request):
    
    if (request.method != 'GET'):
        return 
    
    txid  = request.GET.get('txid')
    value = request.GET.get('value')
    status = request.GET.get('status')
    addr = request.GET.get('addr')

    invoice = Invoice.objects.get(address = addr)
    
    invoice.status = int(status)
    if (int(status) == 2):
        invoice.last_amount = value
        if (invoice.received):
            invoice.received += float(value)
        else:
            invoice.received = float(value)
    invoice.txid = txid
    invoice.save()
    return HttpResponse(200)

def send_image(request):
    if (request.method != 'POST'):
        return 
    address = request.POST.get('addr')
    invoice_obj = Invoice.objects.get(address = address)
    data = {
        'url':invoice_obj.product.product_image,
    }
    return HttpResponse(json.dumps(data), content_type='application/json')