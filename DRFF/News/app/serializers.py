from rest_framework import serializers
from .models import *

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"

class RegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = "__all__"


class NewAccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = NewAccount
        fields = "__all__"



class PulSerializers(serializers.ModelSerializer):
    class Meta:
        model = Money
        fields = "__all__"


class AdvertsimentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Advertsiment
        fields = "__all__"



class DiscountSerializers(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = "__all__"


class SaleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = "__all__"



