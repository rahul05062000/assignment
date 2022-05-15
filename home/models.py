from django.db import models
from django.forms import CharField
from requests import request

# Create your models here.
class item(models.Model):
    name=models.CharField(max_length=50)
    s_no=models.CharField(default=0,max_length=50)
    price=models.CharField(max_length=50)
    details=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class bill(models.Model):
    s_no=models.CharField(default=0,max_length=50)
    item1_quantity=models.CharField(max_length=50)
    
class print(models.Model):
    item_name=models.CharField(max_length=50)
    item_quantity=models.CharField(max_length=50)
    item_price=models.CharField(max_length=50)
    item_total=models.CharField(max_length=50,default=0)

    def __str__(self):
        return self.item_name
    


    

