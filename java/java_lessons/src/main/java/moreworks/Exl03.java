package moreworks;

import static moreworks.Stuff_hwrk.readDigit;

public class Exl03 {
    public static void main(String[] args) {
        System.out.print("Какое треугольное число сгенерировать? ");
        int n = readDigit(), sum, mult;

        for (int i = 1; i <= n; i++) {
            sum = 0;
            mult = 1;
            System.out.printf("T%s: ", i);
            for (int j = 1; j <= i; j++) {
                sum += j;
                mult *= j;
                System.out.printf("%s + ", j);
            }
            System.out.printf("\b\b\b = %s, F%s!=%s\n", sum, i, mult);
        }
    }
}
