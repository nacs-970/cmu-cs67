// 670510681 Atithep Thepkij
import java.util.*;

public class Lab01_2 {
  public static void main(String[] args) {

    Scanner kb = new Scanner(System.in);
    int in = kb.nextInt();

    int sum = in, count = 0, remain = 0, change = 0;

    if (in >= 5){
      // find exceed bottle
      remain = in%5;
      in -= remain;

      change = (in/5)*2;
      sum += change;

      // add exceed back for next calculation
      change += remain;
      count++;
    }

    while (change >= 5) {

      remain = change%5;
      change -= remain;

      change = (change/5)*2;
      sum += change;

      change += remain;
      count++;
    }

    System.out.printf("%d %d %d\n", sum, count, (sum%5));
  }
}
