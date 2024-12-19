// Atithep Thepkij
// 670510681
// Lab05_2 
// 204114 Sec 003

import java.util.Scanner;
public class Lab05_2 {

    public static void compareWeightbase(Person p1, Person p2){ //เมท็อดภายนอกคลาส Person 
        int diff1 = Math.abs(p1.getWeight() - p1.getStandardWeight()); 
        int diff2 = Math.abs(p2.getWeight() - p2. getStandardWeight()); 
        if (diff1 == diff2) System.out.println("both"); 
        else 
            if (diff1 < diff2) System.out.println(p1.getName()); 
            else System.out.println(p2.getName()); 
    }// end method compareWeightbase() 
 
    public static void main(String[] args) { 
        Scanner input = new Scanner(System.in);    
        String s = input.next().trim(); 
        Person p1 = new Person(s);    // create  an object  p1  
        char sex = input.next().charAt(0);   
        int H = input.nextInt(); 
        int W = input.nextInt(); 

        p1.setInfo(sex, H, W); 
        s = input.next().trim(); 
        sex = input.next().charAt(0);   
        Person p2 = new Person(s, sex, input.nextInt(),  input.nextInt()); // create an object  p2 

        compareWeightbase(p1, p2);   //เรียกใช้เมท็อดภายนอกคลาส Person 
    } // end method main() 
} //end class Lab05_2   

class Person {

  private char sex;
  private int height;
  private int weight;
  private String name;

  public Person(String name, char sex, int height, int weight){
    this.name = name;
    this.sex = sex;
    this.height = height;
    this.weight = weight;
  }

  public  Person(String name) {
    this.name = name;
  }

  public void setInfo(char sex, int height, int weight) {
    this.sex = sex;
    this.height = height;
    this.weight = weight;
  }

  public int getWeight() {
    return weight;
  }

  public String getName() {
    return name;
  }

  public int getStandardWeight() {
    if (Character.toUpperCase(sex) == 'M') return height - 100;
    else return height - 110;
  }
}
