// Atithep Thepkij
// 670510681
// Lab06_2
// 204114 Sec 003

import java.util.Scanner;
public class Lab06_2 {

  private static Timestamp readTimestamp(Scanner input) {
    String strInput [] = input.nextLine().trim().split(":");

    int day = Integer.valueOf(strInput[0]);
    int hour = Integer.valueOf(strInput[1]);
    int minute = Integer.valueOf(strInput[2]);
    int second = Integer.valueOf(strInput[3]);

    return new Timestamp(day, hour, minute, second); //return object
    }

  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);

    Timestamp timeA = readTimestamp(input); // datatype = Timestamp
    Timestamp timeB = readTimestamp(input);

    Timestamp result = timeA.diff(timeB);  //result = timeA - timeB 
    System.out.println(result.toString());
  }
}

class Timestamp {

    // member data 
    private int day;
    private int hour;
    private int minute;
    private int second;
    private int cal_second;

    // Inital constructor
    public Timestamp(int day, int hour, int minute, int second) {
      this.day = day;
      this.hour = hour;
      this.minute = minute;
      this.second = second;
      this.cal_second = (int) (second + (60 * minute) + (Math.pow(60,2) * hour) + (Math.pow(60,2) * 24 * day));
    }

    // Result constructor
    public Timestamp(int totalSecond){
      this.day = Math.floorDiv(totalSecond, (60 * 60 * 24));
      totalSecond %= (60 * 60 * 24);
      this.hour = Math.floorDiv(totalSecond, (60 * 60));
      totalSecond %= (60 * 60);
      this.minute = Math.floorDiv(totalSecond, (60));
      this.second = (totalSecond % 60);
    }

    // operators minus such as  timeC =  timeA - timeB
    public Timestamp diff(Timestamp compare) {
      int timeA = this.cal_second;
      int timeB = compare.cal_second;

      int Max_ = Math.max(timeA,timeB);
      int Min_ = Math.min(timeA,timeB);

      int timeC = Max_ - Min_;

      //System.out.println(Max_);
      //System.out.println(Min_);
      //System.out.println(timeC);

      return new Timestamp(timeC); // return type is Timestamp
    }

    @Override
    public String toString() {
      return String.format("%d:%02d:%02d:%02d", day, hour, minute, second);
    }
}
