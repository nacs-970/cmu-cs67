// Atithep Thepkij
// 670510681
// Lab05_1 
// 204114 Sec 003

import java.util.Scanner;

public class Lab05_1 {
  public static void main(String[] args) {

    Bottle cylinder1 = new Bottle("Size02", 2, 6);
    cylinder1.calVolume();

    double r,h;
    Bottle cylinder2 = new Bottle();
    cylinder2.setData();
    cylinder2.calVolume();

    System.out.println("1st constructor");
    cylinder1.displayValue();
    System.out.println("2nd constructor");
    cylinder2.displayValue();

  }
}

class Bottle {
  private String name;
  private double radius;
  private double height;
  private double ans;
  Scanner kb = new Scanner(System.in);

  public Bottle() {}
  public Bottle(String name, double radius, double height) {
    this.name = name;
    this.radius = radius;
    this.height = height;
  }

  public void setData() {
    this.name = kb.nextLine();
    this.radius = Double.valueOf(kb.next());
    this.height = Double.valueOf(kb.next());
  }

  public void calVolume() {
    ans = Math.PI * Math.pow(radius,2) * height;
  }

  public void displayValue() {
    System.out.printf("%s %.1f\n", name, ans);
  }
}
