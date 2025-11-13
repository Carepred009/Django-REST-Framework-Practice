
from django.urls import path

from .views import ProductListCreateAPIView, CategoryListAPIView, ProductUpdateAPIView, ProductDeleteAPIView, \
    product_page

urlpatterns  = [

    path('category_list/', CategoryListAPIView.as_view(), name="category_list"),

    #url path to display the the retrieve from backend to frontend
    path('',product_page,name="product_display"), # HTML FRONTEND
    #We will us this url path fetch sample data in js for frontend
    path('product_list/',ProductListCreateAPIView.as_view(), name="product_list"),


    path('update_product/<int:pk>/', ProductUpdateAPIView.as_view(), name="update_product"),
    #for delete
    path('delete_product/<int:pk>/', ProductDeleteAPIView.as_view(), name="delete_product")


]

