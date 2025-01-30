from django.db import models


class Category(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False)

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id})"

    def __str__(self):
        return f"id: {self.id}, name: {self.name}"
