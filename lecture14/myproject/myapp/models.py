from django.db import models


TYPE_CHOICES = [
    # DB value, Display Value
    ["Action", "ACTION"],
    ["Fiction", "FICTION"],
    ["Horror", "HORROR"],
    ["Comedy", "COMEDY"],
]


class Movie(models.Model):
    name = models.CharField(max_length=40)
    type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    release_date = models.DateField()

    def __str__(self) -> str:
        return self.name
