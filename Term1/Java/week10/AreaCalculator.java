public class AreaCalculator {
    public int squareArea(int side) {
        return side*side;
    }

    public int rectangleArea(int width, int length) {
        return width*length;
    }

    public int triangleArea (int base, int height) {
        return (base*height)/2;
    }
    public float CircleArea (float  radius) {
        return radius*radius*3.14f;

        // Also need to change the class to double
        // final float pi = 3.14f;
        // return Math.pow((radius*pi),2);
    }
}
