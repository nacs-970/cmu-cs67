import java.util.Scanner;
import java.util.Arrays;

public class Lec {

  System.out.println("Basic Syntax");

  public static void variable() {
    int x = 10;
    System.out.println("This is int x " + x);
    x += 1;
    System.out.println("This also is int x " + x);

    String str = new String("ABC"); // prevent duplicate when call variable
    System.out.printf("This is string \"%s\"\n", str);
    System.out.println("---");

    System.out.println("Explicit Casting");
    int a;float b;
    b = a = (int)12.74;
    System.out.println(b);

    int cost;
    cost = (int)(2.7+4.5); System.out.println(cost);
    System.out.println("---");

    System.out.println("Math");
    x = 10/3; System.out.println(x);
    float f;
    f = 10/3; System.out.println(f);
    f = 10.0f/3; System.out.println(f); // f = (float)(10.0/3)
    System.out.println("---");

    System.out.println("Priority");
    b = 5; a = 10 + (int)b++ * 2;
    System.out.println("a: "+ a +" b: "+(int)b);

    b = 5; a = 10 + (int)++b * 2;
    System.out.println("a: "+ a +" b: "+(int)b);

    System.out.println("-------------");
  }

  public static void input() {

    Scanner sc = new Scanner(System.in);

    System.out.print("What is your name? : ");
    String namez = sc.nextLine();
    System.out.printf("Nice to met you %s.\n",namez);

    System.out.println("-------------");
  }

  public static void JavaAppEx1() {
    double x = 2.0, y;
    System.out.println("Hello");
    y = Math.sqrt(x);
    System.out.println("Square root of " + x + " is " + y);
    System.out.println("-------------");
  }

  public static void JavaAppEx2() {

    int[] nums = new int[5]; int i,sum = 0; // array
    Scanner kb = new Scanner(System.in);

    for(i=0;i<=4;i++){
      System.out.print("> ");
      nums[i] = kb.nextInt();
      sum += nums[i];
    }

    System.out.println(Arrays.toString(nums)); // imprt Arrays from util
    System.out.println(sum);
    System.out.println("-------------");
  }

  public static void JavaAppEx3() {
    String pname;int Qty;double price;
    Scanner sc = new Scanner(System.in);

    System.out.print("Input Product Name: ");
    pname = sc.nextLine();

    System.out.print("Input Quantity: ");
    Qty = sc.nextInt();

    System.out.print("Input Price per Unit: ");
    price = sc.nextDouble();

    System.out.printf("%s %d Units ",pname,Qty);
    System.out.printf("Price per Unit is %.2f$ \n", price);
    System.out.printf("Total Amount is %.2f$ \n", Qty*price);

    System.out.println("-------------");
  }

  public static void JavaAppEx4() {
    Scanner kb = new Scanner(System.in);

    System.out.print("Input Number 1: ");
    //int num1 = kb.nextInt();
    float num1 = kb.nextFloat();

    System.out.print("Input Number 2: ");
    //int num2 = kb.nextInt();
    float num2 = kb.nextFloat();

    System.out.println("Sum: "+ (num1 + num2));
    System.out.println("-------------");
  }

  public static void JavaAppEx5() {
    Scanner kb = new Scanner(System.in);
    System.out.print("Enter Char: ");
    char x = kb.nextLine().charAt(0);
    System.out.println("Char: "+x);
    System.out.println("-------------");
  }

  public static void main(String[] args) {
    variable();
    input();
    JavaAppEx1();
    JavaAppEx2();
    JavaAppEx3();
    JavaAppEx4();
    JavaAppEx5();
  }
}
