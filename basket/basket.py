

class Basket():

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('session-key')
        if 'session-key' not in request.session:
            basket = self.session['session-key'] = {}
        self.basket = basket

    def add(self, product):
        product_id = product.id

        if product_id not in self.basket:
            self.basket[product_id] = {'price': float(product.price)}

        self.session.modified = True
