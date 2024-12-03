// Atithep Thepkij (Tun)
// 670510681
// Lab04_5
// 204114 Sec 003

import java.util.Scanner;

public class Lab04_5 {
  static Scanner kb = new Scanner(System.in);
  public static void main(String[] args) {

    int people = kb.nextInt();
    kb.nextLine(); // clear newline
    
    // Set up
    Enrollment[] person = new Enrollment[people];
    
    for(int i = 0; i < people; i++){

      String name = kb.nextLine();

      int num = kb.nextInt();
      kb.nextLine();

      String ids = kb.nextLine().trim();

      person[i] = new Enrollment(name, num, ids);
    }

    String key = kb.nextLine();
    int count = 0;
    for (int i = 0; i < people; i++) {
      //person[i].displaySubject();
      boolean match = person[i].findMatch(key);
      if (match) {person[i].displayName(); count++;}
    } 
    System.out.println(count);
  }
}

class Enrollment{

  String name;
  int number_subjects;
  String subjects_id;

  Enrollment(String name, int number_subjects, String subjects_id){
    this.name = name;
    this.number_subjects = number_subjects;
    this.subjects_id = subjects_id;
  }

  public boolean findMatch(String key){
    boolean check = false;
    String arrStr[] = subjects_id.trim().split(" ");
    for (String str : arrStr) {
      if (str.equals(key)){ check = true; break;}
    }
    return check;
  }

  public void displayName() {
    System.out.println(name);
  }

  public void displaySubject() {
    System.out.println(subjects_id);
  }

}
