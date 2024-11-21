/*  Atithep Thepkij (Tun)
    670510681
    Lab01_3
    204114 sec 003 */

import java.util.*;

public class Lab01_3 {
  public static void main(String[] args) {

    Scanner kb = new Scanner(System.in);
    int size = kb.nextInt();
    int [] array = new int[size];

    for(int i = 0; i <= size-1; i++){
      array[i] = kb.nextInt();
    }
    int key = kb.nextInt();

    boolean empty = true;

    for(int i = 0; i <= size-1; i++){
      if (array[i] >= key){
        System.out.print(array[i] + " ");
        empty = false;
      }
      if (i==size-1 && empty){
        System.out.println("-");
      }
    }

    if(!empty){
      System.out.println();
    }

    empty = true;

    for(int i = 0; i <= size-1; i++){
      if (array[i] < key){
        System.out.print(array[i] + " ");
        empty = false;
      }
      if (i==size-1 && empty){
        System.out.println("-");
      }
    }

    System.out.println();
  }
}