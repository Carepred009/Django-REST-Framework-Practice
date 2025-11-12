
from django.urls import path

from .views import ProductListCreateAPIView, CategoryListAPIView, ProductUpdateAPIView, ProductDeleteAPIView

urlpatterns  = [

    path('category_list/', CategoryListAPIView.as_view(), name="category_list"),

    path('product_list/',ProductListCreateAPIView.as_view(), name="product_list"),
    path('update_product/<int:pk>/', ProductUpdateAPIView.as_view(), name="update_product"),
    #for delete
    path('delete_product/<int:pk>/', ProductDeleteAPIView.as_view(), name="delete_product")


]

