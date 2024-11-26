/*  Atithep Thepkij (Tun)
    670510681
    Lab02_4
    204114 sec 003 */

import java.util.*;
public class Lab02_4 { 
  static Scanner kb = new Scanner(System.in); // global variable

  public static void main(String[] args) {
    int sizeA = kb.nextInt();
    int sizeB = kb.nextInt();
    int[] arrayA = getData(sizeA);
    findAinB(arrayA, sizeB);
  }

  public static int[] getData(int arraysize) {
    int[] array = new int[arraysize];
    for(int i = 0; i< arraysize; i++){
      array[i] = kb.nextInt();
    }
    return array;
  }

  public static void findAinB(int[] arrayA, int sizeB) {

    int[] arrayB = getData(sizeB);
    int max = arrayA[0];

    for(int i = 0; i < arrayA.length; i++){
      int count = 0;
      int compare = arrayA[i];
      for(int j = 0;j < sizeB; j++){
        if(arrayB[j] == compare){
          count++;
        }
      }
      System.out.print(count + " ");
      if(compare > max){
        max = compare;
      }
    }
    System.out.println();
    System.out.println(max);
  }
}
// 3 12 5 7 2 1 7 7 7 2 8 7 2 9 20 15 7
// 4 2 12 7 20 2 33 7

