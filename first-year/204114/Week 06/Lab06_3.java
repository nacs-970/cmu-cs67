// Atithep Thepkij
// 670510681
// Lab06_3
// 204114 Sec 003

import java.util.Scanner;
public class Lab06_3 {
  public static void main(String[] args) {
    Scanner kb = new Scanner(System.in);

    TimeStamp timeA = new TimeStamp(kb.next().charAt(0), kb.nextLine());
    TimeStamp timeB = new TimeStamp(kb.next().charAt(0), kb.nextLine());
    char operator = kb.nextLine().charAt(0);

    // See Lab06_2
    TimeStamp result = timeA.calculate(timeB, operator);
    char displayType = kb.nextLine().charAt(0);
    result.displayResult(displayType);
  }
}

class TimeStamp{

  private char type;
  private int totalSecond;

  // inital constructor
  TimeStamp(char type, String time){
    this.type = Character.toUpperCase(type);
    if (this.type == 'R') this.totalSecond = Integer.valueOf(time.trim());
    else if (this.type == 'T'){
      String tmp_time[] = time.trim().split(" ");
      this.totalSecond += Integer.valueOf(tmp_time[3]);
      this.totalSecond += (Integer.valueOf(tmp_time[2]) * 60);
      this.totalSecond += (Integer.valueOf(tmp_time[1]) * 60 * 60);
      this.totalSecond += (Integer.valueOf(tmp_time[0]) * 60 * 60 * 24);
    }
  }

  // result constructor
  TimeStamp(int result){
    this.totalSecond = result;
  }

  public TimeStamp calculate(TimeStamp compare, char operator) {
    int timeA = this.totalSecond;
    int timeB = compare.totalSecond;
    int result = 0;
    if (operator == '+') result = timeA + timeB;
    else if (operator == '-') result = timeA - timeB;
    
    if (result <= 0) result = 0;
    return new TimeStamp(result);
  }

  public void displayResult(char displayType) {
    displayType = Character.toUpperCase(displayType);
    if (displayType == 'R') System.out.println(totalSecond);
    else if (displayType == 'T'){
      int day, hour, minute, second;

      day = Math.floorDiv(this.totalSecond, (60 * 60 * 24));
      this.totalSecond %= (60 * 60 * 24);

      hour = Math.floorDiv(this.totalSecond, (60 * 60));
      this.totalSecond %= (60 * 60);

      minute = Math.floorDiv(this.totalSecond, (60));
      second = this.totalSecond % (60);

      System.out.printf("%d:%02d:%02d:%02d\n", day, hour, minute, second);
    }
  }
}
