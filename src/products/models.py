from django.db import models

class product(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.FloatField()
    summary = models.TextField(default = 'this is cool!')