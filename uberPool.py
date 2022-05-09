from car import Car     # From file car import class Car

class UberPool(Car):        # Subclass UberPool that inherits attributes from class Car 
    brand = str         # Subclass's attributes
    model = str

    def __init__(self, license, driver, brand, model):          # Constructor methods that receives attributes like parameters license and driver 
        super().__init__(license, driver)                         # from super class Car 
        self.brand = brand 
        self.model = model
