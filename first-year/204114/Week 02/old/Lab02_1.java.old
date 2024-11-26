/*  Atithep Thepkij (Tun)
    670510681
    Lab02_1
    204114 sec 003 */

import java.util.Scanner;
public class Lab02_1 { 

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        char mode = sc.next().charAt(0);
        String symb = sc.next();
        int n = sc.nextInt(); 

        if(Character.isLowerCase(mode)){
          printStartDown(n, symb);
        }

        else if(Character.isUpperCase(mode)){
          printStartUp(n, symb);
        }

        else{
          printStartBoth(n, symb);
        }
    }
    private static void printStartDown(int n,String symb) {	
      //System.out.println("Down");
      for(int i = 0; i<= n;i++){
        for(int j = (n-i); j>0;j--){
          System.out.print(symb + "");
          if(j==1){
            System.out.println();
          }
        }
      }
    }

    private static void printStartUp(int n,String symb) {
      //System.out.println("Up");
      for(int i = 0; i < n;i++){
        for(int j = (n-(i+1)); j > 0; j--){
          System.out.print(" ");
        }
        for(int j = 0;j < (i+1); j++){
          System.out.print(symb + "");
        }
        System.out.println();
      }
    }

    private static void printStartBoth(int n,String symb) {
      //System.out.println("Both");

      // Up
      for(int i = 0; i < n;i++){
        for(int j = (n-(i+1)); j > 0; j--){
          System.out.print(" ");
        }
        for(int j = 0;j < (i+1); j++){
          System.out.print(symb + "");
        }
        System.out.println();
      }
      // Down
      for(int i = 1; i<= n;i++){
        for(int j = (n-i); j>0;j--){
          System.out.print(symb + "");
          if(j==1){
            System.out.println();
          }
        }
      }
    }
}
