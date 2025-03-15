import java.util.Scanner;

public class CurrencyConverter {
    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);

        final float ExchangeRate = 35.95f, MoneyAmount, Convert;

        System.out.print("\nSelect Currency You Want To Convert :\n\nUSD\t---------->\tBAHT\t=\t" + ExchangeRate + " THB" + "\n\n[1] THB -> USD | [2] USD -> THB\t : ");
        int option = scanner.nextInt();

        switch (option) {
            case 1 -> {
                System.out.print("\nEnter THB Amount : ");
                MoneyAmount = scanner.nextFloat(); 
                Convert = MoneyAmount / ExchangeRate;
                System.out.println("You Have Exchanged To " + String.format("%.2f", Convert) + " USD");
            }
            case 2 -> {
                System.out.print("\nEnter USD Amount : ");
                MoneyAmount = scanner.nextFloat(); 
                Convert = MoneyAmount * ExchangeRate;
                System.out.println("You Have Exchanged To " + String.format("%.2f", Convert) + " THB");
            }
            default -> System.out.println("Wrong Option Input!!!!");
        }
        scanner.close();
    }
}