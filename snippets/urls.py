from django.urls import path
from .views import homePageView
from snippets.views import *
urlpatterns = [
    path("", homePageView, name="home"),
    path("order/", listOrders, name="listOrders"),
    path("order/add/", addOrder, name="addOrder"),
]
