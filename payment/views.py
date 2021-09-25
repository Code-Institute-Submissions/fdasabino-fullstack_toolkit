import stripe
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from basket.basket import Basket

@login_required
def BasketView(request):
    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.', '')
    total = int(total)
    
    stripe.api_key = 'pk_test_51JdcCvLxCavNaE0z8e1Ef5xTfVgdLoa87K7EjtWMhu66bH0fncbVYJPji3E4M3CUPq9rQuU0g4z8jDiRpdS4p1Oy003t5zqzFT'
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='SEK',
        metadata={'user_id': request.user.id}
    )
    
    return render(request, 'payment/payment_form.html', {'client_secret': intent.client_secret})
        