

from rest_framework import serializers
from .models import Product,Category, Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


#we will use this for Vue.js display
class  CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

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
        fields = ['id','name','price','category_id','category', 'description']

