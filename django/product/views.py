from django.shortcuts import render
from product.models import Product
from category.models import Category


def get_products(request):
    category = request.GET.get('category')
    context = {}
    if category:
        context['products'] = Product.objects.filter(category__name=category)
    else:
        context['products'] = Product.objects.all()
    context['categories'] = Category.objects.all()
    return render(request, 'products.html', context)
