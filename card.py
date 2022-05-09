from calendar import c
from payment import Payment

class Card(Payment):
    card_number = str
    date = str
    cvv = int 
    
    def __init__(self, ID, card_number, date, cvv):
        super().__init__(ID)
        self.card_number = card_number
        self.date = date
        self.cvv = cvv