// Atithep Thepkij (Tun)
// 670510681
// Lab04_6
// 204114 Sec 003

import java.util.Scanner;

public class Lab04_6 {
  static Scanner kb = new Scanner(System.in);
  public static void main(String[] args) {

    int people = kb.nextInt();
    kb.nextLine();

    double avg = 0;

    University[] student = new University[people];
    for (int i = 0; i < people; i++) {
      String id = kb.next();                           
      int Mscore = kb.nextInt();                       
      int Fscore = kb.nextInt();                       
      kb.nextLine();

      avg += (Mscore + Fscore);                        

      student[i] = new University(id, Mscore, Fscore); 
    }

    avg /= people;

    String searchYear = kb.next();
    String searchFaculty = kb.next();
    int count = 0, count_moreAvg = 0;

    for(int i = 0; i < people; i++){
      boolean checkyear = student[i].findMatchYear(searchYear);
      boolean checkfaculty = student[i].findMatchFaculty(searchFaculty);
      if ( !(checkyear && checkfaculty) ) continue;
      student[i].calScore();
      student[i].displayStudent();
      if (student[i].getScore() > avg) count_moreAvg++;
      count++;
    }
    if (count > 0) System.out.printf("%d\n%d\n", count, count_moreAvg);
    else System.out.println("None");
  }
}

class University{

  String student_id;
  int Mscore;
  int Fscore;
  private int sum;

  University(String student_id, int Mscore, int Fscore){
    this.student_id = student_id;
    this.Mscore = Mscore;
    this.Fscore = Fscore;
  }

  public boolean findMatchYear(String year) {
    String sliced_id_year = student_id.substring(0,2);
    if (sliced_id_year.equals(year)) return true;
    return false;
  }  

  public boolean findMatchFaculty(String faculty) {
    String sliced_id_faculty = student_id.substring(2,4);
    if (sliced_id_faculty.equals(faculty)) return true;
    return false;
  }

  public void calScore() {
    sum = (Mscore + Fscore);
  }

  public void displayStudent() {
    System.out.println(student_id + " " +sum);
  }

  public int getScore() {
    return sum;
  }

}
//5
//610510444 34 48
//620510111 25 15
//610510333 22 35
//620210444 24 36
//610510222 45 45
//61 05
