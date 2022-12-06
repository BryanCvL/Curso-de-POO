from car import Car

if __name__ == "__main__":
    print("Hola Mundo")
    car = Car()
    car.license = "CLS234"
    car.driver = "Andres Cabrera"
    car.passenger = 4
    print(vars(car))

    car2 = Car()
    car2.license = "PF5932"
    car2.driver = "Marta Revello"
    car2.passenger = 3
    print(vars(car2))