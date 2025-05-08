import java.util.Scanner;dpublic class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int i = 1;
        System.out.print("Enter Mulitiply Number : ");
        int num = sc.nextInt();
        
        while(i<=10){
            System.out.printf("%d X %d = %d\n", num, i, num*i);
            i++;
        }
        sc.close();
    }
}