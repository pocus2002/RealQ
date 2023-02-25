from django.db import models

# Create your models here.

class Item(models.Model):

    name = models.CharField('name', max_length=255)
    description = models.TextField('description')
    price = models.IntegerField('price')
    stock = models.IntegerField('stock')
    image = models.ImageField('image', default='None.jpg')

    def __str__(self):
        return self.name
