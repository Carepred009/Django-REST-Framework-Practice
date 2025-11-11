
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

# Create your views here.

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('id') # add order_by
    serializer_class = ProductSerializer


