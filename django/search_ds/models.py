from django.db import models


class Item(models.Model):
    item_id = models.IntegerField(default=0)
    description = models.CharField(max_length=500)
    brand = models.CharField(max_length=100)
