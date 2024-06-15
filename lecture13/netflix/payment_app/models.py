from django.db import models


class Card(models.Model):
    number = models.CharField(max_length=16)
    owner_name = models.CharField(max_length=300)
    expiry_date =  models.DateField()
    cvv = models.CharField(max_length=10)
    bank = models.CharField(max_length=30)

    def __str__(self):
        return self.owner_name
    

class User(models.Model):
    name = models.CharField(max_length=32)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    birth_date = models.DateTimeField()
    is_indian = models.BooleanField()
    skills = models.TextField()
