from re import A
from account import Account

class Driver(Account):

    def __init__(self, ID, name, document, email, password):
        super().__init__(ID, name, document, email, password)