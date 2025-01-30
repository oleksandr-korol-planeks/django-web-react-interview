import uuid
from django.contrib import messages
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from order.forms import CreateOrderForm
from user.models import CustomUser
from product.models import Product
from order.models import Order
from rest_framework.views import APIView
from order.serializers import OrderSerializer
from user.serializers import CustomUserSerializer


def get_orders(request):
    context = {}
    form = CreateOrderForm()
    orders = Order.objects.all()
    context['orders'] = orders
    context['form'] = form
    return render(request, 'orders.html', context)


def create_order(request, pk):
    context = {}
    product = Product.objects.get(pk=pk)
    if request.method == "POST":
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            user = CustomUser.objects.filter(email=request.POST.get('email')).first()
            if not user:
                user = CustomUser.objects.create_user(first_name=request.POST.get('first_name'),
                                                      email=request.POST.get('email'),
                                                      password=uuid.uuid4().hex)

            order = form.save(commit=False)
            order.user = user
            order.product = product
            order.save()
            messages.success(request, f"Order for {request.POST.get('first_name')} has been created")

    else:
        form = CreateOrderForm()
    context['create_order_form'] = form

    return render(request, 'create_order.html', context)


def get_ajax_form(request, pk):
    form = CreateOrderForm()
    return render(request, 'create_ajax_order.html', context={'form': form, 'pk': pk})


class OrderAPIList(APIView):

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        email = request.data.get('email')
        user_data = {
            'first_name': request.data.get('first_name'),
            'email': request.data.get('email'),
            'password': uuid.uuid4().hex
        }
        serializer = CustomUserSerializer(data=user_data)
        if serializer.is_valid():
            user = CustomUser.objects.filter(email=email).first()
            if not user:
                user = serializer.save()

            data = {
                'user': user.id,
                'product': request.data.get('product')
            }
            serializer = OrderSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






