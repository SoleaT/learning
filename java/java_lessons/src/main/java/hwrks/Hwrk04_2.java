package hwrks;

import java.util.LinkedList;
import java.util.List;

public class Hwrk04_2 {
    public static void main(String[] args) {
        LinkedList<String> workArray = new LinkedList<>(List.of("a1", "b2", "c3", "d4", "e5", "f6", "g7"));
        System.out.println(workArray);
        reverseLL(workArray);
        System.out.println(workArray);
    }

    private static void reverseLL(LinkedList<String> workArray) {
        for (int i = 0; i < workArray.size()-1; i++) {
            workArray.add(i, workArray.getLast());
            workArray.removeLast();
        }
    }
}
