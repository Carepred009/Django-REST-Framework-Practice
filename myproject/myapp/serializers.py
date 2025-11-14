

from rest_framework import serializers
from .models import Product,Category

class  CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

class ProductSerializer(serializers.ModelSerializer):
    #category_name = serializers.StringRelatedField(source='category', read_only=True) #uses __str__ of Category
    category = CategorySerializer(read_only=True) # Nested Serializer
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category', #this the field name for FK in the Product model
        write_only= True
    )
    class Meta:
        model = Product
        fields = ['name','price','category_id','category', 'description']

