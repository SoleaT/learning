package hwrks;

import java.util.ArrayList;
//import java.util.Iterator;

import static hwrks.Stuff_hwrk.formArray;
import static hwrks.Stuff_hwrk.readDigit;

public class Hwrk03_1 {
    public static void main(String[] args) {
        System.out.print("Какого размера список создать? ");
        int arrSize = readDigit();
        int maxNumber = 100;

        ArrayList<Integer> tempList = formArray(arrSize, maxNumber);
        System.out.printf("Сформирован список: \u001B[31m%s \u001B[0m\n", tempList);



        //с итератором.
//        Iterator<Integer> listForEdit = tempList.iterator();
//        while (listForEdit.hasNext()) {
//            int elem = listForEdit.next();
//            if (elem % 2 ==0) {
//                listForEdit.remove();
//            }
//        }
        //а вот и незачем с итератором
        tempList.removeIf(x -> x % 2 == 0);
        System.out.printf("После удаления чётных чисел: \u001B[36m%s \u001B[0m\n", tempList);
    }
}
