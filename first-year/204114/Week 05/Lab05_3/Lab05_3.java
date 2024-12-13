// Atithep Thepkij
// 670510681
// Lab05_3
// 204114 Sec 003

import java.util.Scanner;
public class Lab05_3 {
  public static void main(String[] args) {
    Scanner kb = new Scanner(System.in);
    Stackmanager stack = new Stackmanager(kb.nextInt()); // init Constructor
    String str;
    int x,y;

    do {
      x = kb.nextInt();

      if (x == 1){
        y = kb.nextInt();
        stack.push(y);
      }
      else if (x == 2) stack.pop();
      else if (x == 3) stack.getTop();
      else if (x == 4) stack.getSize();
      else if (x == 5) stack.show();
    }while (x != 6);
  }
}

class Stackmanager {
  private int maxSize;
  private int[] item;
  private int top = -1;

  public Stackmanager(int maxSize){
    this.maxSize = maxSize;
    item = new int[maxSize];
  }
  
  public void push(int x) {
    if (!isFull()) item[++top] = x;
    else System.out.println("full");
    
  }
  
  public void pop(){
    if (!isEmpty()) {
      System.out.printf("pop %d\n", item[top]);
      //item[top--] = 0;
      top--;
    }
    else System.out.println("empty");

  }

  public void getTop(){
    if (isEmpty()) System.out.println("empty");
    else System.out.println(item[top]);
  }

  public int getSize(){
    System.out.println(top+1);
    return top+1;
  }

  private boolean isEmpty() {
    if (top == -1) return true;
    return false;
  }

  private boolean isFull() {
    if (top == (maxSize - 1)) return true;
    return false;
  }

  public void show() {
    if (!isEmpty()){ 
      for(int i=0;i<=top;i++) System.out.print(item[i]+" "); 
      System.out.println(); 
    }
    else System.out.println("empty");    
  }  
}
//5 5 1 1 1 2 1 3 5 1 4 1 5 5 6
