from django.shortcuts import render

from rest_framework import generics
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


# Create your views here.

#for Category only Listing the data category



class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def product_create(request):
    return render(request,'myapp/product_create.html')



#display for Vue
def display_category(request):
    return render(request,'DRF_Vue/DRF_Vue_display.html')

#Will use this for now fetch with js script
#We will use this for Vue.js
class CategoryListAPIView(generics.ListAPIView):
    #queryset = Category.objects.all().order_by('id')  will use this for Pytest
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None  # disable pagination


#this the function view for the display to the data retrieve bay backend
def product_page(request):
    return  render(request, 'myapp/product_display.html')

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('id') # add order_by
    serializer_class = ProductSerializer

#we will use this for fetch update in html template
class ProductUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def product_update(request):
    return render(request,'myapp/product_update.html')


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

'''
 #For specific product by id
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
'''

