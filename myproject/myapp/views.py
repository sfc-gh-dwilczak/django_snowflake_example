from django.http import JsonResponse
from .snowflake_utils import get_snowflake_engine
from django.shortcuts import render

def product_list(request):
    engine = get_snowflake_engine()
    with engine.connect() as connection:
        result = connection.execute("SELECT * FROM product").fetchall()
        products = [dict(row) for row in result]
        return JsonResponse(products, safe=False)

def order_list(request):
    engine = get_snowflake_engine()
    with engine.connect() as connection:
        result = connection.execute("SELECT * FROM orders").fetchall()
        orders = [dict(row) for row in result]
        return JsonResponse(orders, safe=False)
    
def home(request):
    engine = get_snowflake_engine()
    with engine.connect() as connection:
        product_result = connection.execute("SELECT * FROM product").fetchall()
        order_result = connection.execute("SELECT * FROM orders").fetchall()

        products = [dict(row) for row in product_result]
        orders = [dict(row) for row in order_result]

    context = {
        'products': products,
        'orders': orders
    }
    return render(request, 'myapp/home.html', context)
