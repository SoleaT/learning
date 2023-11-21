package org.example;

import java.util.*;

public class Main {
    private static final int arrSize = 20;

    public static void main(String[] args) {
//        readName();
        System.out.println();
        int[] arr = formArray();
        System.out.println(Arrays.toString(arr));
        System.out.printf("Самая длинная последовательность из 1: %s", countSequence(arr));

    }

    private static int countSequence(int[] tempArr) {
        int j = 0, k = 0;
        for (int value : tempArr) {
            if (value == 1) {
                j++;
                k = Math.max(j, k);
            } else {
                j = 0;
            }
        }
        return k;
    }

    private static int[] formArray() {
        Random rnd = new Random();
        int[] tempArr = new int[arrSize + 1];
        for (int i = 0; i <= arrSize; i++) {
            tempArr[i] = rnd.nextInt(0, 2);
        }
        return tempArr;
    }


    private static void readName() {
        System.out.println("Введите имя: ");
        String name;
        Scanner readL = new Scanner(System.in);
        name = readL.nextLine();
        System.out.printf("Привет, %s", name);
    }


}