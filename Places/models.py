from django.db import models

# Create your models here.


class Places(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=25, default ='General' )
    price = models.CharField(max_length=5, default='$')
    sponsored = models.BooleanField(default= False)
    hours = models.CharField(max_length=100)
    image_url = models.CharField(max_length=2083)
    rating = models.FloatField(max_length=10)
    description = models.CharField(max_length=500)

# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     event = models.CharField(max_length=200)
#     category = models.CharField(max_length=25, default='General' )
#     price = models.FloatField()
#     sponsored = models.BooleanField(default= False)
#     hours = models.CharField(max_length=100)
#     image_url = models.CharField(max_length=2083)
#     rating = models.FloatField(max_length=10)
#     description = models.CharField(max_length=500)
#
# class Offer(models.Model):
#
#     code= models.CharField(max_length=20)
#     event = models.CharField(max_length=200)
#     description = models.CharField(max_length=500)
#     discount = models.FloatField()
#




