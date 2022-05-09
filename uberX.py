from car import Car     # From file car import class Car.

class UberX(Car):       # Subclass that inherits attributes from super class
    brand = str     # Class attributes
    model = str

    def __init__(self, license, driver, brand, model):      # Constructor method with its parameters
        super().__init__(license, driver)
        self.license = license
        self.driver = driver
