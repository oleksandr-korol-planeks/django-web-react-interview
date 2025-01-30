from django.db import models
from user.models import CustomUser
from product.models import Product
from category.models import Category


class Order(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id})"

    def __str__(self):
        return f"id: {self.id}, user: {self.user}, product: {self.product}"
