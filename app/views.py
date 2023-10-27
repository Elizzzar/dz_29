from django.shortcuts import render
from django.views.generic import CreateView,ListView
from .models import Products, Customer
from django.urls import reverse_lazy
from .forms import Form_Customers, Form_Products

class Create_products(CreateView):
    model = Products
    form_class = Form_Products
    template_name = 'products_create.html'
    success_url = reverse_lazy('dashboard')

class Create_customers(CreateView):
    model = Customer
    form_class = Form_Customers
    template_name = 'customer_create.html'
    success_url = reverse_lazy('dashboard')

class Dashboard(ListView):
    model = Customer
    template_name = 'dashboard.html'
    context_object_name = 'customers'

    def get_queryset(self):
        return Customer.objects.all(), Products.objects.all()