package hwrks;

import java.util.Arrays;
import java.util.Random;

public class Hwrk01_1 {
    private static int arrSize = 20, minDigit = 1, maxDigit = 99;

    public static void main(String[] args) {
        int[] arr = formArray();
        System.out.println(Arrays.toString(arr));
        int min = arr[0], max = arr[0];
        for (int i = 0; i < arr.length - 1; i++) {
            if (arr[i] < min) {
                min = arr[i];
            }
            if (arr[i] > max) {
                max = arr[i];
            }
        }
        System.out.printf("Минимальное число в массиве: %d, максимальное число в массиве: %d", min, max);
    }

    private static int[] formArray() {
        Random rnd = new Random();
        int[] tempArr = new int[arrSize + 1];
        for (int i = 0; i <= arrSize; i++) {
            tempArr[i] = rnd.nextInt(minDigit, maxDigit + 1);
        }
        return tempArr;
    }

}
