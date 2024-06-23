from django.db import models

class Item(models.Model):
    name=models.TextField()
    count=models.IntegerField()
    cost=models.IntegerField()
    description=models.TextField()
# Create your models here.
