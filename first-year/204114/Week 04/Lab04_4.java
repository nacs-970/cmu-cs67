// Atithep Thepkij (Tun)
// 670510681
// Lab04_4
// 204114 Sec 003

import java.util.Scanner;
public class Lab04_4 {
  static Scanner kb = new Scanner(System.in);
  public static void main(String[] args) {
    Encode encode = new Encode();

    int size = encode.size;
    String input = "";

    String str = kb.next();
    str = str.toLowerCase();
    int str_size = str.length();

    //System.out.println(Math.floor(str_size/size));

    for (int i = 0; i < str_size; i+=3) {
      boolean check = encode.checkLength(i, str_size);

      if (check){
        input = str.substring(i,str_size);
        encode.encodeASCII(input);
      }

      else {
        input = str.substring(i,i+3);
        encode.encodeASCII(input);
      }
    }
    encode.displayStr();
  }
}

class Encode {
  public int size = 3;
  private int ascii;
  private String str = "";

  public boolean checkLength(int i, int max_size) {
    if (max_size % 3 != 0 && i + 3 > max_size) return true;
    return false;
  }

  public void encodeASCII(String str) {
    int str_size = str.length();

    for (int i = 0; i < str_size; i++) {

      ascii = (int)str.charAt(i) + 3;
      if (ascii > 122) ascii = (ascii % 122) + 96; // exceed

      this.str += Character.toUpperCase((char)ascii); // add string to instance instead of local variable this.variable
    }
    this.str += "#".repeat(3 - str_size);
    this.str += " ";
  }

  public void displayStr() {
    System.out.println(str.trim());
  }
}
//killhimbeforesunset 
//readmailnow
//usenewgun
