// Atithep Thepkij (Tun)
// 670510681
// Lab04_3
// 204114 Sec 003


// NOT FINISH
import java.util.Scanner;
import java.util.ArrayList;

public class Lab04_3 {
  static Scanner kb = new Scanner(System.in);
  public static void main(String[] args) {

    Number rank = new Number();
    int input;

    do {
      input = kb.nextInt();
      if (input > 100 || input < 1) continue;
      rank.addData((int)input);
      rank.setMinMax();
    } while (input != 0);

    rank.calAvg();
    rank.countBelowAvg();
    rank.displayData();
  }
}

class Number {

  private ArrayList<Integer> numbers = new ArrayList<>();
  private int min, max, count;
  private double avg;

  public void addData(int value) {
    numbers.add(value);
  }

  public void setMinMax() {
    if (min == 0 && max == 0){
      min = numbers.get(0);
      max = numbers.get(0);
    }
    for (int num : numbers) {
      if (num < min) min = num;
      if (num > max) max = num;
    }
  }

  public void calAvg() {
    avg = 0;
    int n = numbers.size();
    for (int num : numbers) avg += num;
    avg /= n;
  }

  public void countBelowAvg() {
    count = 0;
    for (int num:numbers) if (num <= avg && numbers.size() > 1) count++;
  }

  public void displayData() {
    System.out.printf("%d %d\n", max, numbers.indexOf(max) + 1);
    System.out.printf("%d %d\n", min, numbers.indexOf(min) + 1);
    System.out.println(count);
    //System.out.println(avg);
  }
}
//10 1000 70 45 10 33 0 
//1 25 101 99 70 30 0
