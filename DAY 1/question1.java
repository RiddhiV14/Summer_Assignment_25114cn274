import java.util.Scanner;

public class question1  {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input value of n
        System.out.print("Enter a number: ");
        int n = sc.nextInt();

        // Calculate sum
        int sum = n * (n + 1) / 2;

        // Display result
        System.out.println("Sum of first " + n + " natural numbers is: " + sum);

        sc.close();
    }
}