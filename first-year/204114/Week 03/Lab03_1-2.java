import java.util.Scanner;
public class Lab03_1 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    Person person = new Person();

    char sex = sc.next().charAt(0);
    float weight = Float.parseFloat(sc.next());
    int height = sc.nextInt();

    person.setHeight(height);
    person.setWeight(weight);
    person.setSex(sex);

    if (person.getSex() == 'm' ) System.out.print("Male ");
    else System.out.print("Female ");
    if (person.isShapeOK()) System.out.println("not OK");
    else System.out.println("OK");
  }
}
class Person {
  private int height; 
  private float weight;
  private char sex;


  boolean isShapeOK() {
    if(weight < 10 || height > 300) return true;
    else if((int)weight > (height-110)) return true;
    return false;
  }

  void setHeight(int height) {
    this.height = height;
  }

  void setWeight(float weight) {
    this.weight = weight;
  }

  void setSex(char sex) {
    this.sex = Character.toLowerCase(sex);
  }

  char getSex(){
    return sex;
  }
}
