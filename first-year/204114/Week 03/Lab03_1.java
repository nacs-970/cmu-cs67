// Atithep Thepkij (Tun)
// 670510681
// Lab03_1
// 204114 sec 003

// MUST COMPILE BEFORE EXECUTE
import java.util.Scanner;

class Person {
  private float weight;
  private int height;
  private char sex;
  private String str = ""; // can't just String str;
  static Scanner kb = new Scanner(System.in);

  public void getData() {
    sex = kb.next().charAt(0); 
    weight = Float.parseFloat(kb.next()); // Because weight can be Integer sometime
    height = Integer.parseInt(kb.next()); // Incase of 160.00
  }

  public void checkBody() { // no input
    sex = Character.toLowerCase(sex);

    if(sex=='m') str += "Male ";
    else str += "Female ";

    if(weight < 10 || height > 300) str += "not OK";
    else if((int)weight > (height-110)) str += "not OK";
    else str += "OK";
    //System.out.println(sex + " " + weight + " " + height);
  }

  public void displayResult(){
    System.out.println(str);
  }
}

public class Lab03_1 {
  static Scanner kb = new Scanner(System.in);
  public static void main(String[] args) {

    Person human = new Person();
    human.getData();
    human.checkBody();
    human.displayResult();
  }
}
