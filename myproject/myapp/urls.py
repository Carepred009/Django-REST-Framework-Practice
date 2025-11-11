
from django.urls import path

from .views import ProductListCreateAPIView, CategoryListAPIView

urlpatterns  = [

    path('category_list/', CategoryListAPIView.as_view(), name="category_list"),
    path('product-list/', ProductListCreateAPIView.as_view(), name="product-list")

]

