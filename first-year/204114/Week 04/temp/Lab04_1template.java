/*
 * Your name 
 * Your Student ID
 */
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
                
            }
        }

        matrix.checkMatrix();
	System.out.println(matrix.getType());
    }
}
class Matrix {
    private int size;
    private int[][] matrix;
    private boolean diagOne = false;
    private char type;

    public void setSize(int n) {
        size = n;
        matrix = new int[n][n];
    }
    public void setMatrix(int i, int j, int data){
	matrix [i][j] = data;

    }
    public void checkMatrix() {



    }

    public char getType() {





	return type;
    }
}