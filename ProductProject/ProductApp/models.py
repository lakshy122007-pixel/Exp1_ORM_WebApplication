from django.db import models
from django.contrib import admin

# Create your models here.
class Product(models.Model):
    Product_Name = models.CharField(max_length=20, help_text = "Enter Product Name")
    Product_ID = models.IntegerField(help_text = "Enter Product ID")
    Manufactured_Place = models.CharField(max_length=20, help_text ="Enter Manufatured Place")
    Date_of_Manufacture = models.DateField()

class ProductAdmin(admin.ModelAdmin):
    list_display=['Product_Name','Product_ID','Manufactured_Place','Date_of_Manufacture']