from account import Account
from car import Car
from payment import Payment
from UberX import UberX
from UberPool import UberPool
from UberBlack import UberBlack
from UberVan import UberVan

if __name__ == "__main__":
    # print("Hola Mundo")

    # carStandard = Car("LOD490", Account("Javier","PR6780","javier123@gmail.com","javier.123"), 4643, 4)
    # print(carStandard)
    uberX = UberX('LOD490', Account("Javier","PR6780","javier123@gmail.com","javier.123"), 4, 'Kia', 'Rio')
    uberPool = UberPool('LV8932', Account("Mario","AA3111","mario22@gmail.com","mario22"), 4, 'Toyota', 'Yaris')
    uberBlack = UberBlack('II0984', Account("Stef","KDJ32","Stef12@gmail.com","12.stef"), 4, 'True', 'Leather')
    uberVan = UberVan('REE455', Account("Juan","VCB677","juan90@gmail.com","juan.90"), 6, 'True', 'Leather')
    # uberX = Car('LOD490', Account("Javier","PR6780","javier123@gmail.com","javier.123"),4)
    # print(uberX.setPassengers(4))
    uberX
    uberPool
    uberBlack
    uberVan
    # uberX
    # print(vars(car))
    # print(vars(car.driver))