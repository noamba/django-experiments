import csv

from search_ds.models import Brand, Item

# with open('search_dataset.csv') as f:
with open('search_dataset.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        brand_obj, _ = Brand.objects.get_or_create(name=row[2])
        obj, _ = Item.objects.get_or_create(item_id=row[0],
                                            description=row[1],
                                            brand=brand_obj)


# Item.objects.all()
