from django.db import models


class Theater(models.Model):
    number = models.IntegerField("Number")
    description = models.TextField("Description")

    def __str__(self) -> str:
        return f"Theater {self.number}"
