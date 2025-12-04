from django.db.models.fields import return_None
from django.shortcuts import render

from rest_framework import generics
from rest_framework.views import APIView

from .models import Book,Product, Category,Item
from .serializers import BookSerializer,ProductSerializer, CategorySerializer, ItemSerializer

#use for frontend sample display
from rest_framework.response import Response
from  rest_framework.decorators import api_view

from rest_framework.permissions import AllowAny, IsAuthenticated

#Access the User model in the admin
from django.contrib.auth.models import User


# Create your views here.

#Display all users use APIView
class DisplayUser(APIView):
    def get(self,request):
        users = User.objects.values("id","username") #gets the field id and username
        return  Response(users)




class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        return  Response({
            "message":"Welcome! You accessed a protected route",
            "user": request.user.username

        })

#for DELETE  DRF+Vue+axios
class ItemDeleteAPIView(generics.DestroyAPIView):
    queryset  =Item.objects.all()
    serializer_class = ItemSerializer

class BookCreateAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#for PUT/PATCH DRF+Vue+axios
class BookRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



#for DRF+Vue+axios
class ItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [AllowAny]  # <-- add this no authenticaion and CSRF Token required for now because we are using Vue not Django templates



#for Category only Listing the data category

#use for frontend sample display
@api_view(['GET'])
def message_list(request):
    data = {
        "message": "Hello from DJANGO REST API!",
        "status": "success"
    }
    return Response(data)



class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def product_create(request):
    return render(request,'myapp/product_create.html')

#Will use this for now fetch with js script
#We will use this for Vue.js
class CategoryListAPIView(generics.ListAPIView):
    #queryset = Category.objects.all().order_by('id')  will use this for Pytest
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None  # disable pagination


#display for Vue
def display_category(request):
    return render(request,'DRF_Vue/DRF_Vue_display.html')




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


