from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=40)
    company = models.CharField(max_length=40)
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.name

