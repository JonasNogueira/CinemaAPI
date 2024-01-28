from django.db import models


class Movie(models.Model):
    name = models.CharField("Name", max_length=100)
    director = models.CharField("Director", max_length=100)
    duration = models.IntegerField("Duration")

    def __str__(self) -> str:
        return self.name
