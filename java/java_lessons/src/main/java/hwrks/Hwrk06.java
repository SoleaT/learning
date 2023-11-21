package hwrks;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

import static hwrks.Stuff_hwrk.readDigit;
import static hwrks.Stuff_hwrk.readStr;

public class Hwrk06 {
    static final String[] notes = new String[]{"Модель ", "Цвет ", "Процессор ", "Диагональ ", "Память "};
    static Map<Integer, String> criteria = new HashMap<>();
    static ArrayList<Notebook> shop = new ArrayList<>();

    public static void main(String[] args) {

        String[] answers = new String[notes.length];
        int i = 0;
        while (true) {
            System.out.printf("Введите данные по ноуту %s \n", ++i);
            for (int j = 0; j < notes.length; j++) {
                System.out.print(notes[j]);
                answers[j] = readStr();
            }
            try {
                shop.add(new Notebook(answers[0], answers[1], Integer.parseInt(answers[3]), answers[2], Integer.parseInt(answers[4])));
            } catch (Exception e) {
                System.out.println("Возникла ошибка во время внесения данных.");
            }
            System.out.println(shop);
            System.out.print("Для продолжения введите q, для заполнения нового экземпляра - любую букву: ");
            if (readStr().equals("q")) {
                break;
            }
        }
        while (true) {
            System.out.println("Поиск: введите цифру, соответствующую необходимому критерию: ");
            for (int j = 0; j < notes.length; j++) {
                System.out.printf("%s - %s\n", j + 1, notes[j]);
            }
            fillCriteria();
            System.out.print("Для продолжения введите q, для задания еще одного критерия - любую букву: ");
            if (readStr().equals("q")) {
                break;
            }
        }
        if (!criteria.isEmpty()) {
            filterNotebook();
        }
    }

    static void printOneNotebook(Notebook note) {
        System.out.printf("Ноутбук модели %s, цвет %s, ОЗУ %sгб, процессор %s, диагональ %s''",
                note.model, note.color, note.memory, note.proc, note.diag);
    }

    static void filterNotebook() {
        for (int i = 0; i < criteria.size(); i++) {
            System.out.printf("По критерию %s: \n",i+1);
            for (int j = 0; j < shop.size(); j++) {
                if (criteria.containsKey(0)) {
                    if (shop.get(j).model.contains(criteria.get(0))) {
                        printOneNotebook(shop.get(j));
                    }
                } else if (criteria.containsKey(1)) {
                    if (shop.get(j).color.contains(criteria.get(1))) {
                        printOneNotebook(shop.get(j));
                    }
                } else if (criteria.containsKey(2)) {
                    if (shop.get(j).proc.contains(criteria.get(2))) {
                        printOneNotebook(shop.get(j));
                    }
                } else if (criteria.containsKey(3)) {
                    if (shop.get(j).diag >= Integer.parseInt(criteria.get(j))) {
                        printOneNotebook(shop.get(j));
                    }
                } else if (criteria.containsKey(4)) {
                    if (shop.get(j).memory >= Integer.parseInt(criteria.get(j))) {
                        printOneNotebook(shop.get(j));
                    }
                }
            }
        }
    }

    static void fillCriteria() {
        int s = readDigit();
        if (s <= 0 || s > notes.length) {
            System.out.println("Нет такого параметра");
        } else {
            System.out.print("Минимальное значение критерия: ");
            String tempCrit = readStr();
            criteria.put(s - 1, tempCrit);
        }
    }
}
