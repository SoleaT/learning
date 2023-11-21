package hwrks;

import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class Stuff_hwrk {
    public static int[] formArray(int arrSize, int minBorder, int maxBorder) {
        Random rnd = new Random();
        int[] tempArr = new int[arrSize + 1];
        for (int i = 0; i <= arrSize; i++) {
            tempArr[i] = rnd.nextInt(minBorder, maxBorder + 1);
        }
        return tempArr;
    }

    public static ArrayList<Integer> formArray(int arrSize, int maxBorder) {
        Random rnd = new Random();
        ArrayList<Integer> tempList = new ArrayList<>();
        for (int i = 0; i < arrSize; i++) {
            tempList.add(rnd.nextInt(maxBorder));
        }
        return tempList;
    }

    public static int readDigit() {
        int temp;
        Scanner readL = new Scanner(System.in);
        temp = readL.nextInt();
        return temp;
    }

    public static String readStr() {
        Scanner readL = new Scanner(System.in);
        return readL.next();
    }
}


