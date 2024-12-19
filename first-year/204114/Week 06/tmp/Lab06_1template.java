import java.util.Scanner;
public class Lab06_1 {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();
        Triangle myTriangle = new Triangle(n);

        char symbolX= input.next().trim().charAt(0);
	char type = input.next().trim().charAt(0);

        myTriangle.draw();
	.....................
        ......................
    }
}
class Triangle{
    //member data 	
    private ...............; //size of triangle
    
    //constructor	
    public Triangle(int N){
     
    }
    //overloaded methods
    void draw(){
    


    }
    void draw(char X){
    


    }

    
   
}
