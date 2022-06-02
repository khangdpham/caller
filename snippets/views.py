from django.shortcuts import render
from django.http import HttpResponse
import time
import datetime
from snippets.models import *
import random 
import string

def addOrder(request):
  order = Order()
  order.order = "{}_{}".format(random.randint(10,999),"".join(random.choices(string.ascii_uppercase,k=5)))
  order.save()
  return HttpResponse("OK")
def listOrders(request):
  orders = Order.objects.all()
  response = []
  for x in orders:
    response.append("{}".format(x.order))
  return HttpResponse(str(response))
def homePageView(request):
    return HttpResponse("Hello, World!")
