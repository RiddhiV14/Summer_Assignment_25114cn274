import java.util.Scanner;

public class question3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input number
        System.out.print("Enter a number: ");
        int n = sc.nextInt();

        int factorial = 1;

        // Calculate factorial
        for (int i = 1; i <= n; i++) {
            factorial = factorial * i;
        }

        // Print factorial
        System.out.println("Factorial of " + n + " is: " + factorial);

        sc.close();
    }
}
