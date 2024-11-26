import java.util.Scanner;

public class Lec {

  static Scanner kb = new Scanner(System.in);
  public static void math_methods() {
    double x = 3.04;
    System.out.println("ceil 3.04: "+Math.ceil(3.04));
    System.out.println("ceil 3.99: "+Math.ceil(3.99));
  }
  
  // No Return abd Sending Argument
  public static void Example1(){
    print_box();
    print_box();
    print_box();
  }

  public static void print_box(){
    System.out.println("****");
    System.out.println("*  *");
    System.out.println("****");
    System.out.println();
  }

  // No return But Sending Argument
  public static void Example2(){
    int w, l; 
    Scanner input = new Scanner(System.in);
    System.out.print( "Input width and length : " );
    w = input.nextInt();
    l = input.nextInt();
    findArea(w,l);
  }
  private static void findArea(int a, int b){
    float area = a*b;
    System.out.println("Area = " + area);
  }

  // Return but no Sending Argument
  public static void Example3(){
    float area = findArea2();
    System.out.println("Area = " + area);
  }

  private static float findArea2(){
    int w,l;
    Scanner input = new Scanner(System.in);
    System.out.println("Input width and length :");
    w = input.nextInt();
    l = input.nextInt();
    return (w*l);
  }
  public static void Example4() {
    int w,l;
    Scanner input = new Scanner(System.in);
    System.out.println("Input width and length :");
    w = input.nextInt();
    l = input.nextInt();
    float area = findArea3(w,l);
    System.out.println("Area = " + area);
  }

  private static float findArea3(int a, int b) {
    return(a*b);
  }

  public static void JavaAppEx2() {
    int []s = new int[5];
    int i, sum=0;
    Scanner kb = new Scanner(System.in);
    System.out.println("input 5 number");
    for (i = 0; i <= 4; i++) {
      s[i] = kb.nextInt();
      sum += s[i];
    }
    display(s);
    System.out.println(sum);
  }

  public static void display(int[] arr) {
    int i;
    for (i = 0; i <= 4; i++) System.out.println(arr[i]); 
  }

  public static void JavaAppEx3() {
    int []s = new int[5];
    getData(s);
    sumAndDisplay(s);
  }

  public static void getData(int[] arr) {
    System.out.println("input 5 number");
    for (int i = 0; i <= 4; i++) arr[i] = kb.nextInt();
  }

  public static void sumAndDisplay(int[] arr) {
    int i, sum=0;
    for (i = 0; i < 5; i++){
      sum += arr[i];
      System.out.println(arr[i]); 
    }
    System.out.println(sum);
  }

  // Global variable & Local variable
  static int a = 10;
  public static void Example5() {
    int y = 30, x = 5;
    System.out.printf("1:a=%d x=%d y=%d\n",a,x,y);
    a = 1;
    System.out.printf("2:%d\n",test(20));
    System.out.printf("3:a=%d x=%d y=%d\n",a,x,y);
  }
  public static int test(int n) {
    int x=2;
    return a + x +n;
    
  }

  // three method
  
  static int x = 10;
  public static void Example6() {
    System.out.println("main (start) -> x:" + x);
    method1();
    System.out.println("main (method1) -> x:" + x);
    method2(x);
    System.out.println("main (method2) -> x:" + x);
    method3();
    System.out.println("main (method3) -> x:" + x);
  }

  public static void method1() {
    x = x+10;
    System.out.println("method1 -> x:"+x);
  }

  public static void method2(int x) {
    x = x+10;
    System.out.println("method2 -> x:"+x);
  }

  public static void method3() {
    int x = 0;
    x = x + 10;
    System.out.println("method3 -> x:"+x);
  }

  // grade
  
  public static void Example7() {
    int score;
    char ans;
    do{
      score = getScore();
      displayGrade(score);
      System.out.print("\nRun Again(Y/N)?:");
      ans = kb.next().charAt(0);
      ans = Character.toLowerCase(ans);
    } while(ans=='y');
  }

  public static int getScore() {
    int score;
    do{
      System.out.print("Input score (0-100): ");
      score = kb.nextInt();
    }while ((score < 0)||(score > 100));
    return score;
  }

  public static void displayGrade(int score) {
    if(score <= 50) System.out.print("Your grade is U(fail)");
    else System.out.print("Your grade is S(pass)");
    
  }

  public static void main(String[] args){
    System.out.println("Java Method");
    //math_methods();
    //Example1();
    //Example2();
    //Example3();
    //Example4();
    Example5();
    Example6();
    Example7();
    JavaAppEx2();
    JavaAppEx3();
  }
}
