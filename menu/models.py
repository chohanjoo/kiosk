from django.db import models

# Create your models here.

class Menu(models.Model):
    shop = 
    name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    desc = 

class Category(models.Model):
    name = models.CharField(max_length=100)

