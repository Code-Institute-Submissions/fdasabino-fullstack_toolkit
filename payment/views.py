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
    
    stripe.api_key = 'sk_test_51JdcCvLxCavNaE0zm5abdkEKUXfpJ6QKXSc6XkidZSqrWQ1fbN18L4sbJLfqnJ6OGisW7VtbFevb8Xfyrs8bfy9n00MYN8fPS9'
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='SEK',
        metadata={'user_id': request.user.id}
    )
    
    return render(request, 'payment/payment_form.html', {'client_secret': intent.client_secret})
        