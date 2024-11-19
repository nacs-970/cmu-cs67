// 670510681 Atithep Thepkij
import java.util.*;

public class Lab01_1 {

    private static void printSolution(int x, int y, int c) {
        
        int tmp = 0, count = 2;
        
        // swap first
        int a = Math.min(x,y);
        int b = Math.max(x,y);

        int sum = (2 * a) + (b + 1);
        System.out.print(a + " " + b + " ");

        while (sum <= c) {
            // print first to prevent exceed value c
            System.out.print(sum+" ");
            count++;

            a = b; b = sum;
            sum = (2 * a) + (b + 1);

        }

        // print the number of elements in this sequence
        System.out.printf("\n%d\n", count);
    }

    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int a = sc.nextInt();  
        int b = sc.nextInt(); 
        int c = sc.nextInt();  

        printSolution(a, b, c);
    }
  
}
