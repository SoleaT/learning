package hwrks;

import java.util.Scanner;

public class Hwrk01_2 {
    public static void main(String[] args) {
        System.out.print("Введите год: ");
        int inputYear = readDigit();
        System.out.println(isBissextile(inputYear));
    }

    private static int readDigit() {
        int temp;
        Scanner readL = new Scanner(System.in);
        temp = readL.nextInt();
        return temp;
    }

    private static boolean isBissextile(int tempNumber) {
        if (tempNumber % 4 == 0 && (tempNumber % 100 != 0 || tempNumber % 400 == 0)) {
            return true;
        } else {
            return false;
        }
    }
}
