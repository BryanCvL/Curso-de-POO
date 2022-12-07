class Car {
    public $id = integer;
    public $license = string;
    public $driver = string;
    public $passengers = integer;

    public function __construct($license,$driver)
    {
        $this->license = $license;
        $this->driver = $driver;
    }
    public function PrintDataCar()
    {
        echo "The name of driver is {$this->$driver->$name} with the license {$this->$license} and document {$this->$driver->$document}"
    }
}