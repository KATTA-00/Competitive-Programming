import java.math.BigInteger;
import java.util.Scanner;

public class Solution {
    public static void main(String args[]) throws Exception {
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        scanner.nextLine(); 

        for (int i = 0; i < num; i++) {
            String a = scanner.nextLine(); // reads string
            String b = scanner.nextLine(); // reads string

            BigInteger val1 = new BigInteger(a);
            BigInteger val2 = new BigInteger(b);
            BigInteger result = val1.multiply(val2);
            System.out.println(result);
        }
    }
}
