from payment import Payment
from account import Account

class Paypal(Payment):
    password = str

    def __init__(self, ID, email, password):
        super().__init__(ID, email)
        self.password = password