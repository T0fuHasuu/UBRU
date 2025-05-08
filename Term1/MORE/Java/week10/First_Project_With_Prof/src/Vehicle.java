public abstract class Vehicle {

    final String name;
    protected int fuel;

    public Vehicle(String name, int fuel) {
        this.name = name;
        this.fuel = fuel;
    }

    public void move() {
        System.out.println("Move");
    }

    public void refuel(int amount) {
        fuel = fuel + amount;
        System.out.println(name + " ,Fill " + fuel);
    }

    public String getName() {
        return name;
    }

    public int getFuel() {
        return fuel;
    }

}

class Car extends Vehicle {

    public Car(String name, int fuel) {
        super(name, fuel);
    }

    @Override
    public void move() {
        System.out.println("Car Moving");
    }

}

class Motorcycle extends Vehicle {


    public Motorcycle(String name, int fuel) {
        super(name, fuel);
    }
    @Override
    public void move () {
        System.out.println(name + " [motocycle] moving ");
    }
    public void Fly () {
        System.out.println(name + " [motocycle] Flying ");
    }

}

class Truck extends Vehicle implements CanCarryGoods {
    
    public Truck(String name, int fuel) {
        super(name, fuel);
    }

    @Override
    public void CarryGoods() {
        throw new UnsupportedOperationException("Not supported yet.");
    }
    
}

class Bus extends Vehicle implements CanCarryPassenger {

    public Bus(String name, int fuel) {
        super(name, fuel);
    }

    @Override
    public void CarryPassenger() {
        throw new UnsupportedOperationException("Not supported yet.");
    }

}

class Train extends Vehicle implements CanCarryPassenger, CanCarryGoods {

    public Train(String name, int fuel) {
        super(name, fuel);
        //TODO Auto-generated constructor stub
    }

    @Override
    public void CarryPassenger() {
        throw new UnsupportedOperationException("Not supported yet.");
    }

    @Override
    public void CarryGoods() {
        throw new UnsupportedOperationException("Not supported yet.");
    }

}