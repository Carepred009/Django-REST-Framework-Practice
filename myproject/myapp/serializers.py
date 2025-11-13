

from rest_framework import serializers
from .models import Product,Category

class  CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField() #uses __str__ of Category

    class Meta:
        model = Product
        fields = ['name','price','category', 'description']

