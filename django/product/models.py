from django.db import models
from user.models import CustomUser
from category.models import Category


class Product(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='products')

    def __repr__(self):
        return f'{self.__class__.__name__}(id={self.id})'

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, price: {self.price}"
