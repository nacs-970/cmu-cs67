import java.util.Scanner;
public class Lab03_1 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        char sex = sc.next().charAt(0);
        float weight = Float.parseFloat(sc.next());
        int height = sc.nextInt();

  
        if (person.getSex() == 'm' )
	     System.out.print("Male ");
	else
             System.out.print("Female ");

        if (person.isShapeOK()) {
            System.out.println("not OK");
        } else {
            System.out.println("OK");
        }
    }
}
class Person {
    private char sex;


    boolean isShapeOK() {
  


    }
    void setHeight(int height) {
   
    }
    void setWeight(float weight) {

    }
    void setSex(char sex) {
     

    }


}
