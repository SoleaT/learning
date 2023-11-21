package online_tasks;

import java.util.Scanner;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.Buffer;

public class program {
    public static void main(String[] args) {
        String s;
        s="схема";
        System.out.println(s);

        // типы данных
        short petelek = 11;
        int ryadov = 353;
        float provoloka = 1.2f;
        double visota = 17.1;
        boolean volosi = 123 <= 321;
        var imya = 1;
        // System.out.println(getType(petelek*ryadov));
        // System.out.println(s.charAt(2));
        // System.out.println(ryadov/petelek);
        // System.out.println(visota/provoloka);
        // System.out.println(ryadov%petelek);
        // System.out.println(visota/ryadov);
        // System.out.println(petelek-- - --petelek);

        //массивы определение
        int[] arr = new int[10];
        arr = new int[] {1,2,3,4,5,6,7,8,9,0};

        int[] arr2[]=new int[2][2];

        // чтение с консоли разных типов данных
        Scanner iScanner = new Scanner(System.in);
        System.out.printf("имя скажите, имя: ");
        String name = iScanner.nextLine();
        System.out.printf("Привет, %s! \n", name);
        System.out.printf("лет скока? ");
        boolean flag = iScanner.hasNextInt();
        System.out.println(flag);
        int age = iScanner.nextInt();
        System.out.printf("ого, аж %d \n", age);
        iScanner.close();

        //форматирование
        String s1 = String.format("%d + %f", petelek, visota);
        System.out.printf("%d + %.2f", imya, visota);

        // файлы
        //общее
        try (FileWriter fw= new FileWriter("namefile",false)) {
            fw.write(s);
            fw.append('\n');
            fw.flush();
        } catch (IOException e) {
            System.out.println("ошибк   ");
        }
        // вариант посимвольно
        FileReader fr= new FileReader("program.java");
        int c;
        while ((c = fr.read()) != -1) {
            char ch = (char) c;
            if (ch =='\n') {
                System.out.println(ch);
            }
        }        
        // вариант построчно
        BufferedReader br = new BufferedReader(new FileReader("filename"));
        String str;
        while ((str=br.readLine())!=null) {
            System.out.printf("== %s ==\n",str);
        }
        br.close();
    }

    static String getType(Object o) {
        return o.getClass().getSimpleName();
    }
}
