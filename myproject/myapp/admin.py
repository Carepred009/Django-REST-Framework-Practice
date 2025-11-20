from django.contrib import admin
from .models import  Book, Product,Category, Item

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Book)