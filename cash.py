from payment import Payment 

class Cash(Payment):
    def __init__(self, ID):
        super().__init__(ID)