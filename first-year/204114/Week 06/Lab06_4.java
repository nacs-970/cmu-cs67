// Atithep Thepkij
// 670510681
// Lab06_4
// 204114 Sec 003

import java.util.Scanner;

public class Lab06_4 {

    static Customer findPerson(String compare_id, Customer[] person){
      for (Customer customer : person)
        if (customer.getId().equals(compare_id)) return customer;
      return null;
    }

  public static void main(String[] args) {
    Scanner kb = new Scanner(System.in);

    int num_customer = kb.nextInt();
    int num_transac = kb.nextInt();
    kb.nextLine();

    Customer[] person = new Customer[num_customer];
    for (int i = 0; i < num_customer; i++) person[i] = new Customer(kb.next(), kb.next(), kb.nextInt());
    kb.nextLine();

    Transaction transac = new Transaction();
    Customer checked_person_a, checked_person_b; // init Customer Class

    for (int i = 0; i < num_transac; i++) {
      String type = transac.checkType(kb.next().charAt(0));

      String id_a = kb.next();
      checked_person_a = findPerson(id_a, person);

      switch (type) {
        case "deposit":
          checked_person_a.deposit(kb.nextInt());
          break;

        case "withdraw":
          checked_person_a.withdraw(kb.nextInt());
          break;

        case "transfer":
          String id_b = kb.next();
          checked_person_b = findPerson(id_b, person);
          checked_person_a.transfer(checked_person_b, kb.nextInt());
          break;
      }
      //kb.nextLine(); // comment when submit grader
    }

    for (int i = 0; i < num_customer; i++) person[i].displayStatus(); 
  }
}

class Customer {
  private String id, name;
  private int money;

  Customer(String id, String name, int money){
    this.id = id;
    this.name = name;
    this.money = money;
  }

  public void deposit(int money){
    this.money += money;
  }

  public void withdraw(int money){
    if (this.money - money >= 100) this.money -= money;
  }

  public void transfer(Customer person2, int money){
    if (this.money - money >= 100){
      this.money -= money;
      person2.money += money;
    }
  }

  public String getId(){
    return this.id;
  }

  public void displayStatus(){
    System.out.printf("%s %s %d\n", id, name, money);
  }
}

class Transaction {
  private char type;

  public String checkType(char type) {
    this.type = Character.toUpperCase(type);
    if (this.type == 'D') return "deposit";
    if (this.type == 'W') return "withdraw";
    if (this.type == 'T') return "transfer";
    return "invalid";
  }
}
