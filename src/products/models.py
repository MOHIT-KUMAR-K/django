from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank= True, null= True)
    price = models.FloatField()
    summary = models.TextField()