// Atithep Thepkij
// 670510681
// Lab06_4
// 204114 Sec 003

import java.util.Scanner;

public class Lab06_5 {

  public static void main(String[] args) {
    Scanner kb = new Scanner(System.in);

    Star[] m_idol = {new Star("Nadech", 1), new Star("Wier", 2), new Star("Mario", 3)};
    Star[] f_idol = {new Star("Aum", 1), new Star("Yaya", 2), new Star("Bella", 3)};

    int num_voter = kb.nextInt();

    Voter[] people = new Voter[num_voter];
    for(int i = 0; i < num_voter; i++){

      String name = kb.next();
      int m_vote = kb.nextInt();
      int f_vote = kb.nextInt();
      //kb.nextLine(); // comment when submit grader

      people[i] = new Voter(name, m_vote, f_vote);

      m_vote = people[i].getmaleNo();
      f_vote = people[i].getfemaleNo();

      addVote(m_idol, m_vote);
      addVote(f_idol, f_vote);
    }

    checkAndPrintVote(m_idol,f_idol);
    printGoodLuckPeople(m_idol, f_idol, people);
  }

  static void addVote(Star[] idols, int voted_num){
    for (Star idol : idols)
      if (idol.getNumber() == voted_num) idol.addVote();
  }

  static void checkAndPrintVote(Star[] m_idols, Star[] f_idols){

    Star top_m = m_idols[0];
    Star top_f = f_idols[0];

    for (Star m_idol : m_idols) {
      if(m_idol.getVote() > top_m.getVote()) top_m = m_idol;
    }

    for (Star f_idol : f_idols) {
      if(f_idol.getVote() > top_f.getVote()) top_f = f_idol;
    }

    System.out.printf("%s %s\n", top_m.getName(), top_f.getName());
  }

  static void printGoodLuckPeople(Star[] m_idols, Star[] f_idols, Voter[] people){
    Star top_m = m_idols[0];
    Star top_f = f_idols[0];

    for (Star m_idol : m_idols) {
      if(m_idol.getVote() > top_m.getVote()) top_m = m_idol;
    }

    for (Star f_idol : f_idols) {
      if(f_idol.getVote() > top_f.getVote()) top_f = f_idol;
    }

    for (Voter person : people) {
      if (person.getmaleNo() == top_m.getNumber() && person.getfemaleNo() == top_f.getNumber())
        System.out.printf("%s ", person.getName());
    }
  }
}

class Star {
  private String name;
  private int number;
  private int vote = 0;

  Star(String name, int number){
    this.name = name;
    this.number = number;
  }

  public void addVote(){
    this.vote++;
  }

  public int getNumber(){
    return this.number;
  }

  public int getVote(){
    return this.vote;
  }

  public String getName() {
    return this.name;
  }
}

class Voter{
  private String name;
  private int maleNo;
  private int femaleNo;

  Voter(String name, int maleNo, int femaleNo){
    this.name = name;
    this.maleNo = maleNo;
    this.femaleNo = femaleNo;
  }

  public int getmaleNo() {
    return this.maleNo;
  }

  public int getfemaleNo() {
    return this.femaleNo;
  }

  public String getName(){
    return this.name;
  }
}
