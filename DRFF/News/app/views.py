from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import *

from .models import *
from .serializers import *


# Create your views here.

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_class = [IsAuthenticated]


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
    permission_class = [IsAuthenticated]

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializers
    permission_class = [IsAuthenticated]


class NewAccountViewSet(viewsets.ModelViewSet):
    queryset = NewAccount.objects.all()
    serializer_class = NewAccountSerializers
    permission_class = [IsAuthenticated]

class MoneyViewSet(viewsets.ModelViewSet):
    queryset = Money.objects.all()
    serializer_class = PulSerializers
    permission_class = [IsAuthenticated]

class AdvertsimentViewSet(viewsets.ModelViewSet):
    queryset = Advertsiment.objects.all()
    serializer_class = AdvertsimentSerializers
    permission_class = [IsAuthenticated]


class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializers
    permisson_class = [IsAuthenticated]


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializers
    permission_class = [IsAuthenticated]



