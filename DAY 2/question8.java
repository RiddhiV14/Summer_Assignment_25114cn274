
    import java.util.Scanner;

public class question8 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int number = sc.nextInt();

        int original = number;
        int reverse = 0;

        // Reverse the number
        while (number != 0) {
            int digit = number % 10;
            reverse = reverse * 10 + digit;
            number = number / 10;
        }

        // Check palindrome
        if (original == reverse) {
            System.out.println("The number is Palindrome");
        } else {
            System.out.println("The number is not Palindrome");
        }

        sc.close();
    }
}
