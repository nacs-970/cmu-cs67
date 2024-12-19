import java.util.Scanner;
public class Lab06_2 {

    private static Timestamp readTimestamp(Scanner input) {

        String strInput [] = input.nextLine().trim().split(":");

        int day = ..................................;
        int hour = .................................;
        int minute = .................................;
        int second = .................................;

        return new Timestamp(day, hour, minute, second); //return object
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        Timestamp timeA = readTimestamp(input);
        Timestamp timeB = readTimestamp(input);

        Timestamp result = timeA.diff(timeB);  //result = timeA - timeB

        System.out.println(result.toString());
    }
}

class Timestamp {
    // member data 
 


    // constructor

    public Timestamp(...........................) {
      
    }

    // constructor
    ......................................................... {
      



    }

    

    // operators minus  suchas  timeC =  timeA - timeB
    public Timestamp diff(...................) {
       




    }

    @Override
    public String toString() {
        return String.format("%d:%02d:%02d:%02d", day, hour, minute, second);
    }
}


