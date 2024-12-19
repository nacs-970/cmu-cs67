// Atithep Thepkij (Tun)
// 670510681
// Lab04_1
// 204114 Sec 003

import java.util.Scanner;
public class Lab04_1 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    
    Matrix matrix = new Matrix();
    int n = sc.nextInt();	
    matrix.setSize(n);	
    int i, j;

    for (i = 0; i < n; ++i) {
      for (j = 0; j < n; ++j) {
        matrix.setMatrix(i,j, sc.nextInt());
      }
    }

    //matrix.displayMatrix(); 
    matrix.checkMatrix();
    System.out.println(matrix.getType());
  }
}
class Matrix {
  private int[][] matrix;
  private boolean diagOne = false;
  private char type;

  public void setSize(int n) {
    matrix = new int[n][n];
  }

  public void setMatrix(int i, int j, int data){
    matrix [i][j] = data;
  }

  public void checkMatrix() {
    boolean up = true, down = true;

    for (int i = 0; i < matrix.length; i++) {
      for (int j = (i+1); j < matrix[i].length; j++) {
        if(matrix[i][j] != 0) up = false;
        if(!up && !down) break;
      }
    }

    for (int i = 0; i < matrix.length; i++) {
      for (int j = (i-1); j >= 0; j--) {
        if(matrix[i][j] != 0) down = false;
        if(!down) break;
      }
    }

    //System.out.println(up + " " + down);
    if (up && down) type = 'I';
    else if (!(up || down)) type = 'O';
    else if (!up) type = 'U';
    else type = 'L';

    if (up && down){
      for (int i = 0; i < matrix.length; i++){
        if(matrix[i][i] != 1) {
          type = 'O';
          break;
        }
      }
    }

  }

  public char getType() {
    return type;
  }

  //public void displayMatrix(){
  //  for (int i = 0; i < matrix.length; i++) {
  //    for (int j = 0; j < matrix[i].length; j++) {
  //      System.out.print(matrix[i][j] + " ");
  //    }
  //    System.out.println();
  //  }
  //}
  //
//5 1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 1
//3 1 2 0 0 1 2 0 0 1
//3 3 0 0 4 6 0 5 7 1
}
