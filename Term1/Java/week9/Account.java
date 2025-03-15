
public class Account {

    private int id;
    private String name;
    private float balance;
    private int pinCode;

    public Account(int id, String name, float balance, int pinCode) {
        this.id = id;
        this.name = name;
        this.balance = balance;
        this.pinCode = pinCode;
    }

    public void info() {
        System.out.printf("\nAccount Name : %s | ID : %d | Balance : %.2f Baht\n\n", name, id, balance);
    }

    public void withdraw(int money, int pinCode) {
        if (this.pinCode == pinCode) {
            float updatedBalance = balance - money;
            if (updatedBalance > 0) {
                balance = updatedBalance;
                System.out.printf("You have withdrawn %d Baht\n", money);
            } else {
                System.out.println("Cannot Proceed");
                System.err.println("Insufficient Balance. Remaining Balance Is : " + balance);
            }
            info();
            System.out.println("\n________TRANSACTION COMPLETED________\n");

        } else {
            System.out.println("\n________TRANSACTION FAILED________\n");
        }
    }

    public void deposit(int money, int pinCode) {
        if (this.pinCode == pinCode) {
            System.out.printf("You have deposit %d Baht into your main account !!!\n", money);
            balance = balance + money;
            info();
            System.out.println("\n________TRANSACTION COMPLETED________\n");
        } else {
            System.out.println("\n________TRANSACTION FAILED________\n");
        }
    }

}
