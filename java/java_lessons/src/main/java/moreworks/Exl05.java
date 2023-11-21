package moreworks;

import java.util.Arrays;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import static moreworks.Stuff_hwrk.readStr;

public class Exl05 {
    public static void main(String[] args) {
        System.out.println("Введите простое выражение для вычисления: число операция число");
        List<Object> expr  = readDatas(readStr().replaceAll(" ",""));
        System.out.println(doCalc(expr));
    }

    public static List<Object> readDatas(String s) {
        Matcher matcher = Pattern.compile("\\W").matcher(s);
        char sym=' ';
        int x=0,y=0;
        if (matcher.find()) {
            sym=matcher.group().charAt(0);
            try {
                x = Integer.parseInt(s.substring(0, matcher.start()));
                y = Integer.parseInt(s.substring(matcher.start()+1));
            } catch (NumberFormatException e) {
                System.out.println("Не удалось прочитать цифры");
                System.exit(1);
            }
        }
        return Arrays.asList(x,y,sym);
    }
    private static int doCalc(List<Object> nums) {
        int z=0,
            x=(int) nums.get(0),
            y=(int) nums.get(1);
        char chcase = (char) nums.get(2);
        switch (chcase) {
            case '+' -> z = x + y;
            case '-' -> z = x - y;
            case '*' -> z = x * y;
            case '/' -> z = x / y;
            default -> System.out.println("Не распознано");
        }
        return z;
    }

}
