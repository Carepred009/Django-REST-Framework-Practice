
from django.urls import path

from .views import ProductListCreateAPIView

urlpatterns  = [

    path('product-list/', ProductListCreateAPIView.as_view(), name="product-list")

]

