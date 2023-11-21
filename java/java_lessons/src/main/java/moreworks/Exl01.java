package moreworks;

import java.util.Random;

import static java.lang.Math.abs;
import static moreworks.Stuff_hwrk.readDigit;

//сформировать многочлен степени k, используются целые + и - числа

public class Exl01 {
    public static void main(String[] args) {
        System.out.print("Введите степень многочлена k: ");
        int k = readDigit(), range = 100;
        System.out.println(createPolynome(k, range));
    }

    private static String createPolynome(int k, int maxNumber) {
        Random rnd = new Random();
        String resultPolynome = "", pref, numstr;
        int tempNumber;
        for (int i = k; i >= 0; i--) {
            tempNumber = rnd.nextInt(maxNumber*2+1) - maxNumber;
            if (tempNumber != 0) {
                pref = tempNumber < 0 ? //минус должен быть всегда, поэтому, если сгенерилось отр. число, то префикс -
                        " - " :
                        resultPolynome.length() == 0 ? " " : " + ";  //а плюс - только если не первый элемент
                numstr = tempNumber==1 | tempNumber==-1 ? "" : ""+abs(tempNumber);
                if (i > 1) {
                    resultPolynome += String.format("%s%sx^%s", pref, numstr, i);
                } else if (i == 1) {
                    resultPolynome += String.format("%s%sx", pref, numstr);
                } else {
                    pref = pref.equals(" - ") & tempNumber == 0 ? "" : pref;
                    resultPolynome += String.format("%s%s", pref, abs(tempNumber));
                }
            }
        }
        return resultPolynome + " = 0";
    }
}
