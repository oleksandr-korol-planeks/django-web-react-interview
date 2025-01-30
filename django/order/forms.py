from django import forms
from order.models import Order
from user.models import CustomUser


class CreateOrderForm(forms.ModelForm):

    first_name = forms.CharField(required=True)
    email = forms.CharField(max_length=100, required=True)

    class Meta:
        model = Order
        fields = ('first_name', 'email')
