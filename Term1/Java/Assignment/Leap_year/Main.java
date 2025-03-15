import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter a Year : ");
        int year = input.nextInt();

        if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
            System.out.println("This is a Leap Year");
        } else {
            System.out.println("This is not a Leap Year");
        }

        input.close();
    }
}
