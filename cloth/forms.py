from django import forms
from .models import OrderCL

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderCL
        fields = ['customer', 'product', 'status']
