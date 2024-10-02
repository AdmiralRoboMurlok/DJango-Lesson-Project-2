from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)

class Employee(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)