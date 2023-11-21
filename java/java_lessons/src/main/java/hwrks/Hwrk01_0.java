package hwrks;

import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class Hwrk01_0 {
    private static int arrSize = 20, minDigit=1, maxDigit=3, inputDigit;
    public static void main(String[] args) {
        System.out.printf("Введите число, которое нужно переместить (%d-%d): ", minDigit,maxDigit);
        inputDigit=readDigit();
        int[] arr = formArray();
        System.out.println(Arrays.toString(arr));
        System.out.println(Arrays.toString(reformatArray(arr)));
    }

    private static int[] formArray() {
        Random rnd = new Random();
        int[] tempArr = new int[arrSize + 1];
        for (int i = 0; i <= arrSize; i++) {
            tempArr[i] = rnd.nextInt(minDigit, maxDigit+1);
        }
        return tempArr;
    }

    private static int[] reformatArray(int[] tempArr) {
        int left=0, right=tempArr.length-1, temp;
        while (left<right) {
            if (tempArr[left]!=inputDigit) {
                left++;
            }
            if (tempArr[right]==inputDigit) {
                right--;
            }
            if (tempArr[left] == inputDigit && tempArr[right]!=inputDigit) {
                temp=tempArr[right];
                tempArr[right]=tempArr[left];
                tempArr[left]=temp;
                left++;
                right--;
            }
        }
        return tempArr;
    }

    private static int readDigit() {
        int temp;
        Scanner readL = new Scanner(System.in);
        temp = readL.nextInt();
        return temp;
    }
}
