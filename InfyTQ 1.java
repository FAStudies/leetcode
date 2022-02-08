import java.util.Scanner;

public class q1 {
    public static boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i <= n / 2; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static int[] getFactors(int n) {
        int[] factors = new int[n];
        int count = 0;
        for (int i = 1; i <= n / 2; i++) {
            if (n % i == 0) {
                factors[count] = i;
                count++;
            }
        }
        return factors;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String str = scanner.nextLine();
        var split = str.split(" ");

        var sum = 0;
        for (String s : split) {
            try {
                sum += Integer.parseInt("" + s.toCharArray()[s.length() - 1]);
            } catch (Exception e) {
            }
        }

        if (isPrime(sum)) {
            System.out.println(sum);
        } else {
            // Reverse var sum
            var sumReverse = 0;
            while (sum > 0) {
                sumReverse = sumReverse * 10 + sum % 10;
                sum /= 10;
            }
            if (isPrime(sumReverse)) {
                System.out.println(sumReverse);
            } else {
                var factors = getFactors(sumReverse);
                System.out.println(factors.length);
            }
        }
        scanner.close();
    }
}
