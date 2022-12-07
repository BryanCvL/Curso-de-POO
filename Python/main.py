from account import Account
from car import Car

if __name__ == "__main__":
    print("Hola Mundo")

    car = Car("LOD490", Account("Javier","PR6780"))
    print(vars(car))
    print(vars(car.driver))