import pytest
from rest_framework.test import APIClient
from myapp.models import Product,Category




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
    response = client.get('/product-list/') # Ensure correct URL (starts with /)

    assert response.status_code == 200
    assert response.data['count'] == 2
    assert len(response.data['results']) == 2
    assert response.data['results'][0]['name'] == "Product A"