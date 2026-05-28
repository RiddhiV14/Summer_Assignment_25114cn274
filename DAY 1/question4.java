import java.util.Scanner;

public class question4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input number
        System.out.print("Enter a number: ");
        int n = sc.nextInt();

        int count = 0;

        // Count digits
        while (n != 0) {
            n = n / 10;
            count++;
        }

        // Print result
        System.out.println("Number of digits: " + count);

        sc.close();
    }
}
