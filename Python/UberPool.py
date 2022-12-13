from car import Car

class UberPool(Car):
    brand = str
    model = str

    def __init__(self, license, driver,setPassengers, brand, model) -> None:
        # super().__init__(license,driver)
        super().printCarData(license, driver, setPassengers)
        self.brand = brand
        self.model = model
        if setPassengers == 4:
            print('Brand: ' + brand + '\nModel: ' + model)
        else:
            print('You must assign 4 passengers')