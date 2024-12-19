.// Atithep Thepkij
// 670510681
// Lab06_1
// 204114 Sec 003

import java.util.Scanner;
public class Lab06_1 {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    int n = input.nextInt();
    Triangle myTriangle = new Triangle(n);
    char symbolX= input.next().trim().charAt(0);
    char type = input.next().trim().charAt(0);
    myTriangle.draw();
    myTriangle.draw(symbolX);
    myTriangle.draw(symbolX, type);
    }
}
class Triangle{
    //member data 	
    private int size; //size of triangle
    
    //constructor	
    public Triangle(int N){
      this.size = N;
    }

    //overloaded methods
    void draw(){
      char symbolX = '*';
      for (int i = 0; i < size; i++) {
        for (int j = 0; j < (i+1); j++) {
          System.out.print(symbolX);
        }
        System.out.println();
      }
    }

    void draw(char symbolX){
      for (int i = 0; i < size; i++) {
        for (int j = 0; j < (i+1); j++) System.out.print(symbolX);
        System.out.println();
      }
    }

    void draw(char symbolX, char type){
      if (Character.toUpperCase(type) == 'L'){
        for(int i = 0; i < size; i++){
          for(int j = 0; j < (size - i); j++) System.out.print(symbolX);
          System.out.println();
        }
      }
      else{
        for(int i = 0; i < size; i++){
          for(int j = size; j > i; j--) System.out.print(" ");
          for(int j = (i+1); j > 0; j--) System.out.print(symbolX);
          System.out.println();
        }
      }
    }
}
