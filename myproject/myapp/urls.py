
from django.urls import path

from .views import ProductListCreateAPIView, CategoryListAPIView, ProductUpdateAPIView, ProductDeleteAPIView, \
    product_page, ProductCreateAPIView,product_create

urlpatterns  = [

    path('category_list/', CategoryListAPIView.as_view(), name="category_list"),

    #for category fetch only

    #url path for POST method in with DRF CreateAPIView and fetch
    path('product_create/',ProductCreateAPIView.as_view(), name="product_create"),

    #url path for displaying html template for display form that accept input
    path('create_page/', product_create, name="product_create"),


    #url path to display the the retrieve from backend to frontend
    path('',product_page,name="product_display"), # HTML FRONTEND
    #We will us this url path fetch sample data in js for frontend
    path('product_list/',ProductListCreateAPIView.as_view(), name="product_list"),


    path('update_product/<int:pk>/', ProductUpdateAPIView.as_view(), name="update_product"),
    #for delete
    path('delete_product/<int:pk>/', ProductDeleteAPIView.as_view(), name="delete_product")


]

