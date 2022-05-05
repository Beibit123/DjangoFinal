from cgi import print_exception
from rest_framework import serializers
from cafe.models import *


class BasicFoodSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name', 'category', 'description', 'price', 'image', 'url', 'available']
    
class SaladSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length = 50)
    category = serializers.CharField(read_only = True)
    description = serializers.CharField(max_length = 250)
    price = serializers.IntegerField()
    image = serializers.CharField(max_length = 500)
    url = serializers.CharField(max_length = 500)
    available = serializers.BooleanField(default = True)
    
    
class SoupSerializer(serializers.ModelSerializer):
    class Meta(BasicFoodSerializer.Meta):
        model = Soup
        fields = BasicFoodSerializer.Meta.fields

class SnackSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length = 50)
    category = serializers.CharField(read_only = True)
    description = serializers.CharField(max_length = 250)
    price = serializers.IntegerField()
    image = serializers.CharField(max_length = 500)
    url = serializers.CharField(max_length = 500)
    available = serializers.BooleanField(default = True)
        
class DessertSerializer(serializers.ModelSerializer):
    class Meta(BasicFoodSerializer.Meta):
        model = Dessert
        fields = BasicFoodSerializer.Meta.fields

    
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'food_id', 'user_id', 'food_category']