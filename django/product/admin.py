from django.contrib import admin
from product.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'categories', 'users')
    search_fields = ['category__name']

    @staticmethod
    def categories(obj):
        return f"{obj.category.name}"

    @staticmethod
    def users(obj):
        return f"{obj.user.first_name} {obj.user.last_name}"


admin.site.register(Product, ProductAdmin)
