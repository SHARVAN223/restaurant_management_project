from django.shortcuts import render
from .model import Menucategory
from .serializers import Menu_Serializer

# Create your views here.


def Menucategory(req):
    data = Menucategory
