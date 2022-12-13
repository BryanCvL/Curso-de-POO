from account import Account

class Car:
    id = int
    license = str
    driver = Account("","","","")
    __passenger = int

    # def __init__(self,license,driver) -> None:
    #     self.license = license
    #     self.driver = driver

    def setPassengers(self, __passenger):
        if __passenger == 4 and __passenger != '':
            return self.__passenger
        else:
            print('You must assign 4 passengers')

    def printCarData(self, license, driver, setPassengers ) -> None:
        self.license = license
        self.driver = driver
        if setPassengers != '':
            print('\nLicense: ' + license + 
                '\nDriver Name: ' + driver.name + 
                '\nPassengers: ' + str(setPassengers))
        else:
            print('You must assign 4 passengers')