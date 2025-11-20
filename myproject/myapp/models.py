

from  django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    #category = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return  self.name

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return  self.name


'''
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)


    def __str__(self):
        return self.name
    
'''