// 670510681 Atithep Thepkij
import java.util.*;

public class Lab01_2 {
  public static void main(String[] args) {

    Scanner kb = new Scanner(System.in);
    int in = kb.nextInt();
    double sum = in, count = 0, remain = 0, change = 0;

    if (in >= 5){
      remain = in%5;
      in -= remain;
      change = ((float)in/5)*2;
      sum += change;
      change += remain;
      count++;
    }

    while (change >= 5) {
      count++;
      remain = change%5;
      change -= remain;
      change = (change/5)*2;
      sum += change;
      change += remain;
    }

    System.out.printf("%d %d %d\n", (int)Math.rint(sum), (int)count, (int)Math.rint(sum)%5);
  }
}
