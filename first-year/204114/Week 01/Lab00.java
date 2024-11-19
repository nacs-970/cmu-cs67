// 670510681 Atithep Thepkij
import java.util.*;

public class Lab00 {
  public static void main(String[] args) {
    Scanner kb = new Scanner(System.in);
    int sum[] = new int[5];int x,y;

    for(int i=0;i<=4;i++){
      x = kb.nextInt();
      y = kb.nextInt();
      sum[i] = x+y;
    }

    for(int i=0;i<=4;i++){
      System.out.println(sum[i]);
    }
  }
}
