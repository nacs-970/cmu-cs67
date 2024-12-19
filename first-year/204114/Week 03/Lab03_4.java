// Atithep Thepkij (Tun)
// 670510681
// Lab03_4
// 204114 sec 003

import java.util.Scanner;

class Time{
  private int second, minute, hour, day;

  public void setTime(int second){
    this.second = second;
  }

  public void convertTime() {
    minute = Math.floorDiv(second, 60);
    second = second % 60;

    hour = Math.floorDiv(minute, 60);
    minute = minute % 60;
    
    day = Math.floorDiv(hour,24);
    hour = hour % 24;
  }

  public int getSec() {
    return second;
  }
  public int getMin() {
    return minute;
  }
  public int getHour() {
    return hour;
  }
  public int getDay() {
    return day;
  }
}

public class Lab03_4 {
  static Scanner kb = new Scanner(System.in);
  public static void main(String[] args) {
    int second = kb.nextInt();

    Time time = new Time();
    time.setTime(second);
    time.convertTime();
    System.out.printf("%d:%02d:%02d:%02d",time.getDay(), time.getHour(), time.getMin(), time.getSec());
  }
}
