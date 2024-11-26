/*  Atithep Thepkij (Tun)
    670510681
    Lab02_3
    204114 sec 003 */

import java.util.*;
public class Lab02_3 { 
  public static void main(String[] args) {
    Scanner kb = new Scanner(System.in); 
    // set Boundary
    int[] one = new int[2];
    int[] two = new int[2];

    one[0] = kb.nextInt();
    one[1] = kb.nextInt();
    two[0] = kb.nextInt();
    two[1] = kb.nextInt();

    int outside = 0, inside = 0, border = 0;

    //set point of interest
    int n = kb.nextInt();
    for(int i = 0; i < n; i++){
      int[] three = new int[2];
      three[0] = kb.nextInt();
      three[1] = kb.nextInt();

      int check = checkBoundary(one,two,three);
      if(check == 0) outside++;
      if(check == 1) inside++;
      if(check == 2) border++;
    }
    System.out.printf("%d %d %d\n",inside, border, outside);
  }
  public static int checkBoundary(int[] one, int[] two, int[] three) {
    // 0 not in, 1 in, 2 on Border
    int x1 = one[0], y1 = one[1];
    int x2 = two[0], y2 = two[1];
    int x3 = three[0], y3 = three[1];

    int xmin = Math.min(x1,x2);
    int xmax = Math.max(x1,x2);
    int ymin = Math.min(y1,y2);
    int ymax = Math.max(y1,y2);

    if(x3 > xmax || x3 < xmin || y3 > ymax || y3 < ymin) return(0);
    if(x3 == xmax || x3 == xmin || y3 == ymax || y3 == ymin) return(2);
    return(1);
  }
}
// -10 5 -2 -3 5 -5 5 -6 6 -3 -2 -5 0 0 3
// ans : 2 1 2
