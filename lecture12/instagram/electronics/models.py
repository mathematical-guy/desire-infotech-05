from django.db import models
from django.db.models import Model, CharField, IntegerField

# Model (Django/Python) -> Table (SQL)
class Phone(Model):
    # def __init__(self, name, price, brand, description):
    #     self.name = name
    #     self.price = price
    #     self.brand = brand
    #     self.description = description

    name = CharField(max_length=255)
    price = IntegerField()
    ram = IntegerField()
    storage = IntegerField()
    rating = IntegerField()
    brand = CharField(max_length=255, blank=True)

    def __str__(self):
        return self.brand + '---' + self.name 


class WashingMachine(Model):
    name = models.CharField(max_length=32)
    brand = models.CharField(max_length=32, null=True, verbose_name="Brand ka Name (Yaha daalo)")

# print('---'*30)
# qs = Phone.objects.all()
# print(qs)
# Phone.objects.create(

# )
# print(qs.query)
# print('---'*30)