"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user.views import home_screen_view, get_users
from product.views import get_products
from order.views import create_order, get_orders, get_ajax_form, OrderAPIList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name="home"),

    path('product/', get_products, name='products'),
    path('product/<int:pk>/order', create_order, name='create_order'),
    path('product/<int:pk>/ajax/', get_ajax_form, name='create_ajax_order'),

    path('order/', get_orders, name='orders'),

    path('user/', get_users, name='users'),

    path('api/order', OrderAPIList.as_view(), name='api_order')
]

