import csv

from search_ds.models import Item

with open('search_dataset.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            obj, created = Item.objects.get_or_create(
                item_id=row[0],
                description=row[1],
                brand=row[2],
                )


Item.objects.all()
