public class breakStatment {

    public static void main(String[] args) {
        int sum=0;
        for (int i = 1; i <= 5; i++) {
            if (i==3) {
                break;
            }
            sum = sum+i;
        }
        System.out.println("sum = "+sum );
    }
}