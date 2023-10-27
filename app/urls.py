from django.urls import path
from app.views import Create_customers, Create_products, Dashboard

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('create_customers/', Create_customers.as_view(), name='create_customers'),
    path('create_products/', Create_products.as_view(), name='create_products'),
]
