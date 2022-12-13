from car import Car

class UberBlack(Car):
    typeCarAccepted = []
    seatsMaterial = []

    def __init__(self, license, driver, setPassengers, typeCarAccepted, seatsMaterial) -> None:
        # super().__init__(license, driver)
        super().printCarData(license, driver, setPassengers)
        self.typeCarAccepted = typeCarAccepted
        self.seatsMaterial = seatsMaterial
        if setPassengers == 4:
            print('Type Car: ' + str(typeCarAccepted) + '\nSeats: ' + str(seatsMaterial))
        else:
            print('You must assign 4 passengers')