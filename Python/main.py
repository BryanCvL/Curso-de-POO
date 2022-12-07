from account import Account
from car import Car
from payment import Payment

if __name__ == "__main__":
    print("Hola Mundo")

    car = Car("LOD490", Account("Javier","PR6780","javier123@gmail.com","javier.123"), 4643)
    print(vars(car))
    # print(vars(car.driver))