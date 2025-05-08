import java.util.Scanner;

public class PassOrFailLoop {
    public static void main(String[] args) {

        // กำหนดตัวแปรต่างๆ
        String name , result , cont;
        int score;
        Scanner misterX = new Scanner(System.in);

        do {
            System.out.print("name : ");
            name = misterX.nextLine();
            System.out.print("score : ");
            score = misterX.nextInt();
            if (score >= 60) {
                result = "pass";
            } else {
                result = "fail";
            }
            System.out.println(name+", you " +result);
            System.out.print("press 'Y' to continue : ");
            cont = misterX.next();
            misterX.nextLine();
        } while (cont.equals("Y") || cont.equals("y"));

        misterX.close();

    }
}
