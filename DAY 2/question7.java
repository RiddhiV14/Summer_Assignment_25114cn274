import java.util.Scanner;

public class question7 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int number = sc.nextInt();

        int product = 1;

        // Find product of digits
        while (number != 0) {
            int digit = number % 10;
            product = product * digit;
            number = number / 10;
        }

        System.out.println("Product of digits = " + product);

        sc.close();
    }
}