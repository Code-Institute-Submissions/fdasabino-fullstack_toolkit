import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AQsZaJWuemHUcpVRv_WE4XlWhgcal6mde-ZhtZHBS2xEd1lSYy59BxgpBNMZ6zKIzg8AsX5NW1PWhsoF"
        self.client_secret = "EOEU4wk1Ng3npNRD_ejKVyIgpNLtm0VnUSUNdUCLwxQ6BZ-QtRbtLetbq6AVI0YYlubqE-Ipy9izMY2P"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)
