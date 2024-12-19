// Atithep Thepkij (Tun)
// 670510681
// Lab04_2
// 204114 Sec 003

import java.util.Scanner;

public class Lab04_2 {
  public static void main(String[] args) {
    Scanner kb = new Scanner(System.in);

    Three_of_kind matrix = new Three_of_kind();
    int n = kb.nextInt();
    matrix.setSize(n);

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        matrix.setMatrix(i, j, kb.nextInt());

        boolean check = matrix.checkValid(i,j);
        //System.out.println(check);
        if (!check) continue;

        int num = matrix.getData(i,j);
        //System.out.println(num);
        matrix.checkThree(num);
      }
    }
    matrix.displayNone();
  }
}

class Three_of_kind {
  private int[][] matrix;

  private String ans = "";
  private boolean empty = true;

  public void setSize(int n){
    matrix = new int[n][n];
  }

  public void setMatrix(int i, int j, int data){
    matrix [i][j] = data;
  }

  public boolean checkValid(int i, int j) {
    int size = matrix.length - 1;

    // border top, bot, left, right
    if (i == 0 || i == size || j == 0 || j == size) return true;

    // diagonal forward, backward
    if (i == j || j == (size - i)) return true;

    return false;
  }

  public void checkThree(int data) {
    if( data > 0 && data <= 999 && data % 111 == 0 ) {
      if (empty) empty = false;
      ans += (data + " ");
    }
  }

  public int getData(int i, int j) {
    return matrix[i][j];
  }

  public void displayNone(){
    if (empty) System.out.println("No");
    else System.out.println(ans.trim());
  }
}

//4 1 70 2222 25 10 444 14 66 50 26 333 16 220 30 84 28
//4 1 777 2222 25 10 15 14 111 555 27 18 16 220 30 888 28
//4 1 70 2222 999 10 40 14 12 50 666 80 16 777 30 84 28
//5 1 333 4444 122 777 12 60 11 25 9 999 61 666 333 222 10 555 6 444 111 30 888 55 60 6666
//4 1 8 2222 25 10 15 14 66 33 27 18 16 220 30 36 28
