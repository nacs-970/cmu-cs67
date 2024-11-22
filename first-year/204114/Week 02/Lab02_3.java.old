/*  Atithep Thepkij (Tun)
    670510681
    Lab02_3
    204114 sec 003 */

import java.util.*;
public class Lab02_3 { 
  public static void main(String[] args) {
    Scanner kb = new Scanner(System.in); 
    // set Boundary
    int x1 = kb.nextInt();
    int y1 = kb.nextInt();
    int x2 = kb.nextInt();
    int y2 = kb.nextInt();
    int outside = 0;
    int inside = 0;
    int border = 0;

    //set point of interest
    int n = kb.nextInt();
    for(int i = 0; i < n; i++){
      int x3 = kb.nextInt();
      int y3 = kb.nextInt();
      int check = checkBoundary(x1,y1,x2,y2,x3,y3);
      if(check == 0){
        outside++;
      }
      if(check == 1){
        inside++;
      }
      if(check == 2){
        border++;
      }
    }
    System.out.println(inside + " " + border + " " + outside);
  }
  public static int checkBoundary(int x1, int y1,int x2 ,int y2, int x3, int y3) {
    // 0 not in, 1 in, 2 on Border
    int xmin = Math.min(x1,x2);
    int xmax = Math.max(x1,x2);
    int ymin = Math.min(y1,y2);
    int ymax = Math.max(y1,y2);
    if(x3 > xmax || x3 < xmin || y3 > ymax || y3 < ymin){
      return(0);
    }
    if(x3 == xmax || x3 == xmin || y3 == ymax || y3 == ymin){
      return(2);
    }
    return(1);
  }
}
