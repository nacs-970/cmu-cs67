// Atithep Thepkij (Tun)
// 670510681
// Lab03_2
// 204114 sec 003

import java.util.Scanner;
class Coures {
  private int times;
  private char type;
  private float sum;
  static Scanner kb = new Scanner(System.in);

  public void setData() {
    type = kb.next().charAt(0);
    type = Character.toLowerCase(type);
    times = kb.nextInt();
    sum = 0;
  }

  public void calPrice() {
    if(type=='m') sum = (times*700);

    else{
      for (int i = 1; i <= times; i++) {
        if(i >= 11) sum += 650.50;
        else if(i >= 6 && i <= 10) sum += 750;
        else if(i >= 2 && i <= 5) sum += 780;
        else sum += 800;
      }
    }
  }

  public void displayValue(){
    System.out.printf("%.2f ", sum);
  }
}
public class Lab03_2 {
  public static void main(String[] args) {
    Coures study = new Coures();

    study.setData();
    study.calPrice();
    study.displayValue();

    study.setData();
    study.calPrice();
    study.displayValue();
  }
}
