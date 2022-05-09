from car import Car         # From file car import class Car

class UberBlack(Car):           # Subclass that inherits attibutes from superclass 
    typeCarAccepted = []            # Object that saves a list
    seatsMaterial = []

    def __init__(self, license, driver, typeCarAccepted, seatsMaterial):            # Constructor method  with attributes like parameters
        super().__init__(license, driver)
        self.typeCarAccepted = typeCarAccepted
        self.seatsMaterial = seatsMaterial
