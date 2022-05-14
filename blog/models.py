from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.AutoField
    ename=models.CharField(max_length=100)
    eloc=models.CharField(max_length=100)
    esal=models.IntegerField()
    def __str__(self):
        return self.ename

class Product(models.Model):
    eid=models.AutoField

    date=models.DateField()
    pname = models.CharField(max_length=100)
    Pprice= models.IntegerField()

    def __str__(self):
        return self.pname

class Product2(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=100)
    product_category=models.CharField(max_length=100)
    product_price=models.IntegerField()
    product_date=models.DateField()
    product_image=models.ImageField(upload_to="blog/image",default="")

    def __str__(self):
        return self.product_name



