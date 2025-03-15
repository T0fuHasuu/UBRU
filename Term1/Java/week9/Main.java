
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int time = 0;
        Account accountNumA = new Account(2251, "Dayuth", 5467.34f, 1234);
        accountNumA.info();

        do {
            System.out.print("Deposit Or Withdraw ? [D/W] : ");
            String Ch = sc.next();

            if (Ch.toLowerCase().equals("d")) {

                System.out.print("How much you want to Deposit ? ");
                int money = sc.nextInt();
                System.out.print("Enter Pincode ? ");
                int pinCode = sc.nextInt();

                accountNumA.deposit(money, pinCode);

            } else if (Ch.equals("w")) {

                System.out.print("How much you want to Withdraw ? ");
                int money = sc.nextInt();
                System.out.print("Enter Pincode ? ");
                int pinCode = sc.nextInt();

                accountNumA.withdraw(money, pinCode);

            } else {
                System.out.println("Invalid Input");
            }
            time++;
        } while (time < 3);

    }
}
