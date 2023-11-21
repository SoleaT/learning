package moreworks;

import java.io.FileReader;
import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Exl02 {
    private int multNum, degree;

    @Override
    public String toString() {
        return " " +
                multNum + "x" +
                "^" + degree;
    }

    public Exl02(int multNum, int degree) {
        this.multNum = multNum;
        this.degree = degree;
    }

    public static void main(String[] args) {
        String filename1 = System.getProperty("user.dir").concat("\\src\\main\\java/moreworks\\exl02_file1.txt"),
                filename2 = System.getProperty("user.dir").concat("\\src\\main\\java\\moreworks\\exl02_file2.txt");
        String readedStr1 = readFromFile(filename1),
                readedStr2 = readFromFile(filename2);
        ArrayList<Exl02> expressions1 = parsePolynome(readedStr1); //на первый второй рассчитайсь
        ArrayList<Exl02> expressions2 = parsePolynome(readedStr2);
        int maxDegree = Math.max(expressions1.get(0).degree, expressions2.get(0).degree);
        int[] expressionsFin = new int[maxDegree + 1];
        System.out.println(expressions1);

        //И ТУТ ЗДОРОВЕННЫЙ КОСТЫЛЬ!
        for (Exl02 item : expressions1) {
            expressionsFin[item.degree] = item.multNum;
        }
        for (Exl02 item : expressions2) {
            expressionsFin[item.degree] += item.multNum;
        }
//        int tempMul,tempDeg; //вдруг придумаю, как без костыля написать

        //суслик сдулся и не сделал красивый вывод
        for (int i = maxDegree; i >= 0; i--) {
            if (expressionsFin[i] != 0)
                System.out.printf("%dx^%d", expressionsFin[i], i);
        }
    }

    private static String readFromFile(String filename) {
        String tempStr = "";
        try (FileReader file1 = new FileReader(filename)) {
            int c;
            while ((c = file1.read()) != -1) {
                tempStr += (char) c;
            }
        } catch (Exception e) {
            System.out.printf("Возникла ошибка %s", e);
            System.exit(0);
        }
        return tempStr;
    }

    private static ArrayList<Exl02> parsePolynome(String parseStr) { //ШТО ЗА АД
        ArrayList<Exl02> exprs = new ArrayList<>();
        parseStr = parseStr.substring(0, parseStr.length() - 4).replaceAll(" ", "");
        Pattern pattern = Pattern.compile("\\W?\\d*x?\\^?\\d*");
        Matcher matcher = pattern.matcher(parseStr);
        String symb, tempStr, tmpMult;
        System.out.println(parseStr);
        int mult = 0, deg;
        while (matcher.find() & matcher.start() < parseStr.length() - 1) {
            //а дальше ад потому, что мне не захотелось создавать паттерн и матчер для каждой запчасти и я разобрала вручную
            //впрочем, не факт, что было б сильно короче. но придётся комменты писать, а то всё забуду
            tmpMult = "";
            tempStr = matcher.group(); //в отдельную строчку - подстроку с выражением
//            System.out.printf("Подстрока: %s|",tempStr);   //debug
            symb = tempStr.substring(0, 1);                  //что там со знаком, он есть?
            if (symb.equals("-") | symb.equals("+")) {       //если был знак, то обрезаем его
                tempStr = tempStr.substring(1);
            }
            if (tempStr.indexOf('x') == -1) {   //если в выражении нет х, то множитель будет равен всей полученной строке
                tmpMult = tempStr;
            } else {
                tmpMult = tempStr.substring(0, tempStr.indexOf('x')); //ну а если есть, то вырезаем множитель
            }
            if (tmpMult.length() > 0) {  //если множитель не равен 1, парсим его в целое число
                try {
                    mult = Integer.parseInt(tmpMult);
                } catch (Exception e) {
                    System.out.printf("Что-то пошло не так: %s", e); // что-то пошло не так
                    System.exit(1);
                }
            } else {
                mult = 0; //а если равен 1, то присваиваем ему 0. Л - логика.
            }
            mult = symb.equals("-") ? -mult : mult; //если был знак -, то надо сделать число отрицательным
            if (tempStr.indexOf('^') != -1) {       //если в выражении есть степень, находим ее
                deg = Integer.parseInt(tempStr.substring(tempStr.indexOf('^') + 1));
            } else if (tempStr.indexOf('x') == -1) { //а если просто число, стало быть, степень = 0
                deg = 0;
            } else {                                 //а если просто x, то степень = 1
                deg = 1;
            }
            exprs.add(new Exl02(mult, deg)); //записываем в список
//            System.out.printf("m %s,d %s ||", mult, deg); //debug
        }
        return exprs;
    }
}
