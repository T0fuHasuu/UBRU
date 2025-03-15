import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int begin,end,sum;

        System.out.println("Finding Rational In Range ");

        System.out.print("Enter Number to Begin : ");
        begin = sc.nextInt();
        System.out.print("Enter Number to Begin : ");
        end = sc.nextInt();

        while ( begin <= end ) {
            sum = begin;
            begin++;
            if ( sum % 2 != 0 ) {
                continue;
            }
            System.out.println(sum);
        }
        sc.close();
    }
}