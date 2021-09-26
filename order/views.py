from django.http.response import JsonResponse
from django.shortcuts import render
from basket.basket import Basket
from .models import Order, OrderItem


def add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':

        order_key = request.POST.get('order_key')
        full_name = request.user.full_name
        baskettotal = basket.get_total_price()

        # Check if order exists
        if not Order.objects.filter(order_key=order_key).exists():
            order = Order.objects.create(full_name=full_name, address1='add1',
                                         address2='add2', total_paid=baskettotal, order_key=order_key)
            order_id = order.pk

            for item in basket:
                OrderItem.objects.create(
                    order_id=order_id, product=item['product'], price=item['price'], quantity=item['qty'])

        return JsonResponse({'success': 'Return something'})


def payment_confirmation(data):
    Order.objects.filter(order_key=data).update(billing_status=True)


def user_orders(request):
    full_name = request.user.full_name
    return Order.objects.filter(full_name=full_name).filter(billing_status=True)
