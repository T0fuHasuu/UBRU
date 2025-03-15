public class World {

    public static void main(String[] args) {
        Horse h1 = new Horse("White Flag", "White");
        Pegasus p1 = new Pegasus("Pega Aero", "Black");

        h1.walk();
        h1.run();

        p1.run();
        p1.walk();
        p1.fly();
    }
}