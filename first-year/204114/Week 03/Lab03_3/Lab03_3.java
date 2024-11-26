// Atithep Thepkij (Tun)
// 670510681
// Lab03_3
// 204114 sec 003

import java.util.Scanner;

// CAN ONLY USE ONE SCANNER
class Grade {

  private int mid_score, final_score, sum_score;
  private String id="", gpx="", str="";
  //static Scanner kb = new Scanner(System.in);

  public void setData(String id, int mid_score, int final_score) {
    this.id = id;
    this.mid_score = mid_score;
    this.final_score = final_score;
    sum_score = (mid_score + final_score);
  }

  public void processGrade() {
    if(sum_score >= 85) gpx="A";
    else if(sum_score >= 80 && sum_score <=84) gpx="B+";
    else if(sum_score >= 75 && sum_score <=79) gpx="B";
    else if(sum_score >= 60 && sum_score <=74) gpx="C+";
    else if(sum_score >= 55 && sum_score <=59) gpx="C";
    else if(sum_score >= 50 && sum_score <=54) gpx="D+";
    else if(sum_score >= 45 && sum_score <=49) gpx="D";
    else gpx="F";
  }

  public void converStr() {
    str = String.format(" %s %d %s", id, sum_score, gpx);
  }

  public String getStr() {
    return str;
  }
  
}
public class Lab03_3 {
  static Scanner kb = new Scanner(System.in);
  public static void main(String[] args) {
    int num,space,i;

    num = kb.nextInt();

    Grade[] student = new Grade[num];
    for (i = 0; i < num; i++) {
      student[i] = new Grade();
      student[i].setData(kb.next(), kb.nextInt(), kb.nextInt());
      student[i].processGrade();
      student[i].converStr();
    }

    space = kb.nextInt();
    for(i = 0; i < num;i++){
      if(i!= 0 && i%space == 0) System.out.println();
      System.out.printf("%d) %s\n", i+1, student[i].getStr());
    }
  }
}
//4 610510111 25 15 610510222 34 48 610510333 30 35 610510444 45 45 5
