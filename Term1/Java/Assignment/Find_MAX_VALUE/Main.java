import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int num1, num2, num3, Max;

        System.out.print("Enter First Number : ");
        num1 = input.nextInt();
        System.out.print("Enter Second Number : ");
        num2 = input.nextInt();
        System.out.print("Enter Third Number : ");
        num3 = input.nextInt();

        Max = ( num1 >= num2 ) ? num1 : num2;
        Max = ( Max >= num3 ) ? Max : num3;
        
        System.out.println("________________________\n");
        System.out.printf("The Highest Number is %d\n", Max);
        System.out.println("________________________");

        input.close();
    }
}