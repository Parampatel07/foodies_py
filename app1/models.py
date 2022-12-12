from django.db import models

# Create your models here.
class admin(models.Model):
    username= models.CharField(max_length=126)
    password= models.CharField(max_length=256)

class shopkeeper(models.Model):
    email = models.CharField(max_length=126)
    password=models.CharField(max_length=256)
    name=models.CharField(max_length=256)
    companyname=models.CharField(max_length=256)
    mobilenum=models.IntegerField(max_length=256)
    image=models.ImageField(max_length=256)
    city=models.CharField(max_length=126)
    desc=models.TextField()
    state=models.CharField(max_length=126)
    isdeleted=models.CharField(max_length=2)
    
class category(models.Model):
    title=models.CharField(max_length=126)
    image=models.CharField(max_length=256)
    shopkeeperid=models.IntegerField(max_length=10)
    isdeleted=models.IntegerField(max_length=2)
    
class user(models.Model):
    email = models.CharField(max_length=126)
    password=models.CharField(max_length=256)
    mobile=models.CharField(max_length=11)
    city=models.CharField(max_length=126)
    address=models.TextField()
    pincode=models.IntegerField(max_length=126)
    
class bill(models.Model):
    fullname=models.CharField(max_length=126)
    city=models.CharField(max_length=126)
    address=models.TextField()
    mobile=models.CharField(max_length=11)
    productid=models.IntegerField(max_length=10)
    userid=models.IntegerField(max_length=10)
    quantity=models.IntegerField(max_length=10)
    payment_mode=models.IntegerField(max_length=2)
    billdate=models.DateTimeField(auto_now_add=True)
    pincode=models.IntegerField(max_length=8)
    total=models.IntegerField(max_length=10)
    
class cart(models.Model):
    productid=models.IntegerField(max_length=10)
    quantity=models.IntegerField(max_length=10)
    billid=models.IntegerField(max_length=10)
    userid=models.IntegerField(max_length=10)


class product(models.Model):
    title=models.CharField(max_length=126)
    price=models.IntegerField(max_length=10)
    desc=models.TextField()
    categoryid=models.IntegerField(max_length=10)
    shopkeeperid=models.IntegerField(max_length=10)
    image=models.CharField(max_length=256)
    bld=models.IntegerField(max_length=2)
    stock=models.IntegerField(max_length=2)
    isdeleted=models.IntegerField(max_length=2)
    