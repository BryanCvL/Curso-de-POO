class Main {
    public static void main(String[] args) {
        System.out.println("Hola Mundo");
        Car car = new Car("AMQ123", new Account("Andres Herrera", "DSA5465"));
        // UberX uberx = new UberX("AMQ123", new Account("Andres Herrera", "DSA5465"), "Hyundai", "Elantra");
        car.printDataCar();

        Car car2 = new Car("CL2577", new Account("Andrea Vargas", "KDL2344"));
        car2.printDataCar();
    }
}