from django.db import models

# Create your models here.

class Products(models.Model):
    name_product = models.TextField()
    price = models.IntegerField()

class Customer(models.Model):
    name = models.TextField()
    gmail = models.EmailField()
    product = models.ManyToManyField(Products, related_name="customers")
    delivery = models.BooleanField()

    def __str__(self):
        return f'{self.name}'