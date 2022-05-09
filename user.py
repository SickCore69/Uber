from account import Account

class User(Account):

    def __init__(self, ID, name, document, email, password):
        super().__init__(ID, name, document, email, password)