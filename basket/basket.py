

class Basket():

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('session-key')
        if 'session-key' not in request.session:
            basket = self.session['session-key'] = {}
        self.basket = basket
