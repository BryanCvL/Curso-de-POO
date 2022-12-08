import java.util.ArrayList;
import java.utils.Map;

class UberBlack extends Car {
    // Map<String, Map<String, Integer>> typeCarAccepted;
    ArrayList<String> seatsMaterial;


    public UberBlack(String license, Account driver/*, Map<String, Map<String, Integer>> typeCarAccepted, ArrayList<String> seatsMaterial */){
        super(license, driver);
        // this.typeCarAccepted = typeCarAccepted;
        // this.seatsMaterial= seatsMaterial;
    }
    @Override
    public void setPassenger(Integer passenger) {
        if (passenger == 4) {
            this.passenger = passenger;
        }else {
            System.out.println("You must assign 4 passengers");
        }
    }
}