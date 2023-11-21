package hwrks;

import java.util.ArrayList;
import java.util.Collections;

import static hwrks.Stuff_hwrk.formArray;

public class Hwrk03_2 {
    public static void main(String[] args) {
        int arrSize = 20, maxNumber = 50;

        ArrayList<Integer> workList = formArray(arrSize, maxNumber);
        System.out.println(workList);
        double avg = 0;
        for (int elem : workList) {
            avg += elem;
        }
        avg = avg / workList.size();
        Collections.sort(workList);
        System.out.printf("Max = %s, Min = %s, Avg = %.2f\n", workList.get(workList.size() - 1), workList.get(0), avg);
    }
}
