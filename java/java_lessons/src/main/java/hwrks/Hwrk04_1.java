package hwrks;

import java.util.ArrayDeque;

import static hwrks.Stuff_hwrk.readStr;

public class Hwrk04_1 {
    public static void main(String[] args) {
        System.out.println("""
                Вводите строки для сохранения
                Команда print выводит список сохраненных строк
                Команда revert удаляет последнюю введённую строку
                q - выход""");
        ArrayDeque<String> inputStrs = new ArrayDeque<>();
        String s;
        while (true) {
            s = readStr();

            if (s.equalsIgnoreCase("q")) {
                System.out.println("Выход");
                break;
            }

            if (s.equals("print")) {
                System.out.println(inputStrs);
            } else if (s.equals("revert")) {
                inputStrs.removeFirst();
            } else {
                inputStrs.addFirst(s);
            }
        }
    }
}
