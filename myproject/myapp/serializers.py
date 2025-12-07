

from rest_framework import serializers
from .models import Book, Product,Category, Item

#this serializer if for PUT/PATCH DRF_VUE_axios
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


#we will use this for Vue.js display
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
        fields = ['id','name','price','created_at','category_id','category', 'description']
