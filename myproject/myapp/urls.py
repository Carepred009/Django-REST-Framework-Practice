from tkinter.font import names

from django.urls import path

from .views import DashboardView, BookCreateAPIView, ItemDeleteAPIView, BookRetrieveUpdateAPIView, ProductListCreateAPIView, CategoryListAPIView, ProductUpdateAPIView, ProductDeleteAPIView, \
    product_page, message_list, ItemListCreateAPIView, ProductCreateAPIView, product_create, product_update, display_category

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns  = [

    #Use for login
    path('api/token/',TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/token/refresh/',TokenRefreshView.as_view(), name="token_refresh"),
    # Use for login
    #from view for login Browsable API.
    path('api/dashboard/', DashboardView.as_view(), name="dashboard"),


    path('create_book/', BookCreateAPIView.as_view(), name="create_book"),
    path('book/<int:pk>/',BookRetrieveUpdateAPIView.as_view(), name="book"),

    #Item DeleteAPIView
    path('item-delete/<int:pk>/', ItemDeleteAPIView.as_view(), name="item-delete"),

    #for ItemCreateAPIView
    path('api/create_item/',ItemListCreateAPIView.as_view(), name="create_item"),
    path('api/create_item/list/',ItemListCreateAPIView.as_view(),name="create_item_list"),


    #use for frontend sample display
    path('api/message/', message_list),

    #We will us this for Vue.js
    path('api/category_list/', CategoryListAPIView.as_view(), name="category_list"),
    #display the category in html template with Vue
    path('display_category/', display_category, name="display_category"),
    #for category fetch only



    #url path for POST method in with DRF CreateAPIView and fetch
    path('product_create/',ProductCreateAPIView.as_view(), name="product_create"),

    #url path for displaying html template for display form that accept input
    path('create_page/', product_create, name="product_create"),


    #url path to display the the retrieve from backend to frontend
    path('',product_page,name="product_display"), # HTML FRONTEND
    #We will us this url path fetch sample data in js for frontend
    path('product_list/',ProductListCreateAPIView.as_view(), name="product_list"),



    #for for Browsable API testing
    path('product_update/<int:pk>/', ProductUpdateAPIView.as_view(), name="update_product"),

    #product displaly from DRF to html template back to DRF
    path('product_update/', product_update, name="product_update"),



    #for delete
    path('delete_product/<int:pk>/', ProductDeleteAPIView.as_view(), name="delete_product")


]

