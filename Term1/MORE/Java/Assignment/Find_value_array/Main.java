import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int size, sum = 0, Low_Value, High_Value;
        double AVG;

        //Input Into Array
        System.out.print("Enter Amount of Input: ");
        size = sc.nextInt();
        int[] values = new int[size];

        for (int i = 0; i < size ; i++) {
            System.out.print("Number " + (i+1) + " : ");
            values[i] = sc.nextInt();
        }

        //Bubble sort
        for (int i = 0; i < size - 1; i++) {
            for (int j = 0; j < size - i - 1; j++) {
                if (values[j] > values[j + 1]) {
                    int temp = values[j];
                    values[j] = values[j + 1];
                    values[j + 1] = temp;
                }
            }
        }
        Low_Value = values[0];
        High_Value = values[size-1];
        
        //Summation and Average it
        for (int i = 0; i < size; i++){
            sum += values[i];
        }
        AVG = sum/2;

        System.out.printf("The Highest Value : %d\t|\t",High_Value);
        System.out.printf("The Lowest Value : %d\t|\t",Low_Value);
        System.out.printf("The Average Value : %.2f",AVG);

    }
}