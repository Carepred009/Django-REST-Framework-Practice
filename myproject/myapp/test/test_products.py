from decimal import Decimal
from http.client import responses
from pydoc import resolve
from tkinter.font import names

import pytest
from django.urls import reverse
from pytest_django.fixtures import client
from rest_framework.test import APIClient
from myapp.models import Product,Category
from  django.contrib.auth.models import User
from unicodedata import category


@pytest.mark.django_db
def test_get_category():
    #create sample Category
    Category.objects.create(name="Clothes")
    Category.objects.create(name="Electronics")

    client = APIClient()
    url = reverse('category_list')

    #Send GET request
    response = client.get('/category_list/') #the same as the url path

    # Check for response data
    assert response.status_code == 200

    # Access the 'results' key because of pagination
    #Whenever DRF pagination is enabled, always use response.json()['results'] to get the list of items.
    data = response.json()['results']
    assert  len(data) == 2
    assert  data[0] ['name'] == "Clothes"
    assert  data[1] ['name'] == "Electronics"

@pytest.mark.django_db
def test_get_products():

    #create category objects
    category1 = Category.objects.create(name="Clothes")
    category2 = Category.objects.create(name="Electronics")


    #Create products objects
   #Product.objects.create(name="Product A", price=2000, category=category1, create_at="", description="WALEY")
   # Product.objects.create(name="Product B", price=3000, category=category2, create_at="", description="WALEY2")
    #we can removed the create_at because it date, auto_now_add=True
    #The django sent auto with this
    Product.objects.create(name="Product A", price=2000, category=category1, description="WALEY")
    Product.objects.create(name="Product B", price=3000, category=category2, description="WALEY2")

    client = APIClient()
    response = client.get('/product_list/') # Ensure correct URL (starts with /)

    assert response.status_code == 200
    assert response.data['count'] == 2
    assert len(response.data['results']) == 2
    assert response.data['results'][0]['name'] == "Product A"


@pytest.mark.django_db
def test_update_product():
    # Create a test user
    user = User.objects.create_user(username='DRF_sample', password='ppp')

    #create the Category for forieng key relationship
    cat1 = Category.objects.create(name="Electronics")

    #Create a test Product first(so we can have something to update)
    product = Product.objects.create(name="LAPAD", price=800, category=cat1, description ="WIDE")

    # prepare the updated data we want to send
    updated_data = {
        "name":"T5 LAPAD",
        "price":700,
        "description":"WIDER"
    }

    #get the url for the UpdateAPIView
    url = reverse('update_product',args=[product.id])

    #create and APIClient (DRF's built-in test client)
    client = APIClient()
    # Force login (simulate authenticated user)
    client.force_authenticate(user=user)

    #send the PUT request to update the Product
    response = client.put(url, updated_data, format='json')

    #AssertionL check that update worked
    assert response.status_code == 200 # expect HTTP 200 ok
    assert response.data['name'] == "T5 LAPAD"
    assert float(response.data['price'] )== 700.00
    assert response.data['description'] == "WIDER"

    #Verify the object in database is also updated
    product.refresh_from_db()
    assert product.name == "T5 LAPAD"
    assert product.price == 700
    assert product.description == "WIDER"