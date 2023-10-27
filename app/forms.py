from django import forms
from .models import Products, Customer

class Form_Products(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('name_product', 'price')

class Form_Customers(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'gmail', 'product','delivery')