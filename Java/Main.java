class Main {
    public static void main(String[] args) {
        // System.out.println("Hola Mundo");
        // Car car = new Car("AMQ123", new Account("Andres Herrera", "DSA5465"));
        UberX uberx = new UberX("AMQ123", new Account("Andres Herrera", "DSA5465"), "Hyundai", "Elantra");
        uberx.setPassenger(4);
        uberx.printDataCar();

        UberPool uberpool = new UberPool("FOD0391", new Account("Carlos Perez", "MNV2908"), "Chevrolet", "Sonic");
        uberpool.setPassenger(4);
        uberpool.printDataCar();

        UberBlack uberblack = new UberBlack("VFI7846", new Account("Juan Iglesias", "RRR4389"));
        uberblack.setPassenger(4);
        uberblack.printDataCar();

        UberVan ubervan = new UberVan("GJD4983", new Account("Pedro Avila", "KOP9000"));
        ubervan.setPassenger(6);
        ubervan.printDataCar();

        // Car car2 = new Car("CL2577", new Account("Andrea Vargas", "KDL2344"));
        // car2.printDataCar();
    }
}