// Atithep Thepkij
// 670510681
// Lab05_4
// 204114 Sec 003

import java.util.Scanner;
public class Lab05_4 {
  public static void main(String[] args) {
    Scanner kb = new Scanner(System.in);
    GPX student = new GPX();
    int num = kb.nextInt();
    for (int i = 0; i < num; i++) {
      student.getData(kb.next().charAt(0), kb.nextInt());
      student.calScore();
    }
    student.calGpa();
  }
}

class GPX {
  private char grade;
  private double gpa;
  private int credit, sum_credit, sum_point, grade_point;

  private int convertGrade(){
    grade = Character.toUpperCase(grade);
    if(grade == 'A') return 4;
    else if(grade == 'B') return 3;
    else if(grade == 'C') return 2;
    else if(grade == 'D') return 1;
    else if(grade == 'F') return 0;
    return 0;
  }

  public void getData(char grade, int credit) {
    this.grade = grade;
    this.credit = credit;
    grade_point = convertGrade();
  }

  public void calScore() {
    int ans = grade_point * credit;
    System.out.printf("%c %d %d %d\n", grade, grade_point, credit, ans);
    sum_credit += credit;
    sum_point += ans;
  }

  public void calGpa() {
    gpa = (double)sum_point/(double)sum_credit;
    System.out.printf("%d %d %.2f", sum_credit, sum_point, gpa);
  }
}
