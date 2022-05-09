from account import Account


class Car:          # Class with its attributes
    ID = int            # Name attribute and datatype that it saves
    license = str
    driver = Account("","")         # In this case driver saves a constructor method with two parameters(name, document)
    passenger = int

    def __init__(self, license, driver):
        self.license = license
        self.driver = driver

