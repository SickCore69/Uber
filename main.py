from account import Account         # From file account import class Account
from car import Car                 # From file car import class Car
                
if __name__ == "__main__":
    uber = Car("ABC123", Account("Jaden Yuki", "FFJY123456"))       # object creation with a method and its minimum parameters 
    uber.passenger = 4
    print(vars(uber))       # Print of all attributes from class Car 
    print(vars(uber.driver))        # Print of method driver from class Account       

    uberPool = Car("XYZ987", Account("Alberto Madriguera", "KFAM123456"))
    uberPool.passenger = 4
    print(vars(uberPool))
    print(vars(uberPool.driver))

    uberBlack = Car("BCD555", Account("Juan Hernandez", "LRJH123456")) 
    uberBlack.passenger = 4
    print(vars(uberBlack))
    print(vars(uberBlack.driver))

    uberVan = Car("QWE666", Account("Felipe Angeles", "SBFA123456"))
    uberVan.passenger = 6
    print(vars(uberVan))
    print(vars(uberVan.driver))