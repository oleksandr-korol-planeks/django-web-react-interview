from django.contrib import admin
from order.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'email', 'product_name', 'category', 'price')

    @staticmethod
    def user_name(obj):
        return obj.user.first_name

    @staticmethod
    def email(obj):
        return obj.user.email

    @staticmethod
    def product_name(obj):
        return obj.product.name

    @staticmethod
    def category(obj):
        return obj.product.category.name

    @staticmethod
    def price(obj):
        return obj.product.price


admin.site.register(Order, OrderAdmin)
