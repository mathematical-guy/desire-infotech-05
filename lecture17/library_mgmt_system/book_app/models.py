from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    pages = models.CharField(max_length=4)

    def __str__(self) -> str:
        return self.title

