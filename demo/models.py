from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=20)
    introduction = models.TextField()
    range = models.CharField(max_length=20)
    item_number = models.IntegerField(default=1)
    viewnum = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    buynum = models.IntegerField(default=0)
    parcelnum = models.IntegerField(default=0)

    def __str__(self):
        return self.name







