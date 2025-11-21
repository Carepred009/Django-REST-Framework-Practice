from decimal import Decimal
from http.client import responses
from itertools import product
from pydoc import resolve
from tkinter.font import names

import pytest
from django.urls import reverse
from pytest_django.fixtures import client
from rest_framework.test import APIClient
from myapp.models import Book, Product,Category, Item
from  django.contrib.auth.models import User
from unicodedata import category

@pytest.mark.django_db
def test_create_Item():

    client = APIClient()

    #Define the data you wan to send
    data = {
        "name":"Item1",
        "description":"Mahal na item"
    }

    #Send Post request to the API endpoint
    url = reverse('create_item') #Make sure your URL name is the same
    response = client.post(url, data, format='json')

    #Assert the API responded with 201 CREATED
    assert response.status_code == 201

    # added this because its working
    # This ensures your API returns correct data AND actually saves it.
    # Catch bugs in either serializer output or saving logic.
    # check the response, It ok to be remove
    assert response.data['name'] == "Item1"
    assert response.data['description'] == "Mahal na item"

    #Assert the object was create in the database
    #check the database
    item = Item.objects.get(name="Item1") #gets the actual data if it match the object, if no match raise error DoesNotExist
    assert item.description == "Mahal na item"  #check if its the actual data inserted


@pytest.mark.django_db
def test_create_book():
    client = APIClient()

    data = {
        "title":"Book1",
        "author":"Love"
    }

    #Send POST request to the API endpoint
    url = reverse('create_book') # make sure your URL name is correct
    response = client.post(url, data, format='json')

    #Asset THE API responded with 201 CREATED
    assert response.status_code == 201

    # added this because its working
    # This ensures your API returns correct data AND actually saves it.
    # Catch bugs in either serializer output or saving logic.
    # check the response, It ok to be remove
    assert response.data['title'] == "Book1"
    assert response.data['author'] == "Love"


    #Assert the object was create in the database
    #check the database
    book = Book.objects.get(title="Book1")
    assert book.author == "Love"

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

    #AssertionL check d update worked
    assert response.status_code == 200 # expect HTTP 200 ok
    assert response.data['name'] == "T5 LAPAD"
    assert float(response.data['price'] )== 700.00
    assert response.data['description'] == "WIDER"

    #Verify the object in database is also updated
    product.refresh_from_db()
    assert product.name == "T5 LAPAD"
    assert product.price == 700
    assert product.description == "WIDER"

@pytest.mark.django_db
def test_delete_product():

    #Create test user
    user = User.objects.create_user(username="DRF_sample", password="ppp")


    #Create the Category because we have foreign key
    cat1 = Category.objects.create(name="Electronics")


    #Create a sample product to test in the database
    product = Product.objects.create(name="LAPTOP", price=900, category = cat1, description="15 inches")

    client = APIClient()
    # Force login (simulate authenticated user)
    client.force_authenticate(user=user)

    url = reverse('delete_product', args=[product.id])

    #Send DELETE request
    response = client.delete(url)

    #Assertions
    assert  response.status_code == 204 # No content (success)
    assert  Product.objects.count() == 0 #Product deleted
