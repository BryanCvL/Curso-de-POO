// function Car(license, driver) {
//     this.id;
//     this.license = license;
//     this.driver = driver;
//     this.passenger;
// }

class Car {
    constructor(license, driver){
        this.id;
        this.license = license;
        this.driver = driver;
        this.passenger;
    }
    // printDataCar = function () {
    //     console.log(this.driver)
    //     console.log(this.license)
    //     console.log(this.driver.name)
    //     console.log(this.driver.document)
    // }
    printDataCar = (license, driver, brand, model) => {
        console.table(this.driver) //imprimirá una tabla con todos los datos
        console.log(this.driver.name)
        console.log(this.driver.document)
        console.log(this.brand)
        console.log(this.model)
    }
}

