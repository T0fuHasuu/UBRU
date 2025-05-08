public class sumDoWhile {
    public static void main(String[] args) {
        int sum=0 , i=0;
        do {
            sum = sum+i;
            i++;
        } while (i<10);
        System.out.println("sum = "+sum);
    }
}