from django.db import models


class Brand(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return "%s" % (self.name)


class Item(models.Model):

    item_id = models.IntegerField(default=0)
    description = models.CharField(max_length=500)
    brand = models.ForeignKey(Brand, blank=True, null=True)

    def __str__(self):
        return "%s: %s, %s" % (self.item_id,
                               self.description,
                               self.brand)
