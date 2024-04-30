from django.urls import path
from .views import product_list, order_list
from myapp.views import home 

urlpatterns = [
    path('products/', product_list, name='product-list'),
    path('orders/', order_list, name='order-list'),
    path('', home, name='home'),
]