from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    price = models.IntegerField()
    
    def __init__(self):
        return self.name + " : " + self.cuisine
    