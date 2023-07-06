from django.db import models

# Create your models here.
class Category(models.Model):
    Category_Name=models.CharField(max_length=70)


class product_model(models.Model):
    Category=models.ForeignKey( Category,on_delete=models.CASCADE,null=True)
    Product_Name=models.CharField(max_length=100)
    Description=models.CharField(max_length=200)
    Quality=models.IntegerField()
    price=models.ImageField()
    manufacture_date=models.DateField(auto_now_add=True)