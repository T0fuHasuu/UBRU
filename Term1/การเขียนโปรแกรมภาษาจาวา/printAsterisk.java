import java.util.Scanner;

public class printAsterisk {
    public static void main(String[] args) {
        
        int col,row;
        Scanner misterX = new Scanner(System.in);
        System.out.print("enter row : ");
        row = misterX.nextInt();
        System.out.print("enter col : ");
        col = misterX.nextInt();

        for (int i = 0; i < row; i++) {
            for (int j = i; j < col; j++) {
                System.out.print("*");
            }
            System.out.println("");
        }
    }

}
