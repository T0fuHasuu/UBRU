import java.util.Scanner;

public class main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int x,y,row;

        System.out.print("Enter Row Value : ");
        row = sc.nextInt();

        for (x = row; x >= 1; x--) {
            for (y = 1; y < x; y++) {
                System.out.print(" ");   //spaces
            }
            for (y = 0; y <= row - x; y++) {
                System.out.print("*");  //aserites
            }
        System.out.println();
        }
        sc.close();
    }
}