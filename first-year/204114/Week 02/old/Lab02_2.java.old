/*  Atithep Thepkij (Tun)
    670510681
    Lab02_2
    204114 sec 003 */

import java.util.*;
public class Lab02_2 { 
  public static void main(String[] args) {
    Scanner kb = new Scanner(System.in);
    int num = kb.nextInt();
    System.out.println(checkOddEven(num));
    System.out.println(checkPrime(num));
    
  }
  public static String checkPrime(int n) {
    if (n < 2){
      return("not prime");
    }

    // eratosthenes
    for (int i = 2; i*i <= n; i++){
      if (n % i == 0){
        return("not prime");
      }
    }
    return("prime");
  }

  public static String checkOddEven(int n) {
    if(n%2 == 1){
      return("odd");
    }
    return("even");
  }
}
