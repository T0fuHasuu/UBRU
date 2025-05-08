public class Main {
    public static void main(String[] args) {
        AreaCalculator ac = new AreaCalculator();

    // square 3x3
    System.out.println(ac.squareArea(3));
    // rectangle 4x5
    System.out.println(ac.rectangleArea(4, 5));
    // triangle base = 4, height = 5
    System.out.println(ac.triangleArea(4, 5));
    // circle radius = 5
    System.out.println(ac.CircleArea(5));
    }
}