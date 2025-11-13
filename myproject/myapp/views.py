from django.shortcuts import render

from rest_framework import generics
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


# Create your views here.
#Will use this for now fetch with js script
class CategoryListAPIView(generics.ListAPIView):
    #queryset = Category.objects.all().order_by('id')  will use this for Pytest
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#this the function view for the display to the data retrieve bay backend
def product_page(request):
    return  render(request, 'myapp/product_display.html')

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('id') # add order_by
    serializer_class = ProductSerializer


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


