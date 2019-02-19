from django.db import models

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name
