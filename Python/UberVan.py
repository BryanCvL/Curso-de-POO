from car import Car

class UberVan(Car):
    typeCarAccepted = []
    seatsMaterial = []

    def __init__(self, license, driver, setPassengers, typeCarAccepted, seatsMaterial) -> None:
        # super().__init__(license, driver)
        super().printCarData(license, driver, setPassengers)
        self.typeCarAccepted = typeCarAccepted
        self.seatsMaterial = seatsMaterial
        if setPassengers == 6:
            print('Type Car: ' + str(typeCarAccepted) + '\nSeats: ' + str(seatsMaterial))
        else:
            print('You must assign 6 passengers')