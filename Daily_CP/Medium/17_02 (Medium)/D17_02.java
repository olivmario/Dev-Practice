import java.util.Random;

public class D17_02{
    public static double Pi(int n) {
        Random random = new Random();
        int inside = 0;
        for (int i = 0; i < n; i++) {
            double x = -1 + 2 * random.nextDouble();
            double y = -1 + 2 * random.nextDouble();
            if (x * x + y * y <= 1) {
                inside++;
            }
        }
        return 4.0 * inside / n;
    }

    public static void main(String[] args) {
        int n = 100;
        System.out.print(Pi(n));
    }
}
