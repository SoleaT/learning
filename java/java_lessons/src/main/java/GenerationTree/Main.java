package GenerationTree;

import java.util.GregorianCalendar;

public class Main {
    public static void main(String[] args) {
        FamilyPerson vasya = new FamilyPerson("Вася", "Пупкин", "Пупкин", new GregorianCalendar(2000, 11, 5), "male");
        FamilyPerson masha = new FamilyPerson("Маша", "Пупкина", "Васильева", new GregorianCalendar(2001, 5, 1), "female");
        FamilyPerson sergay = new FamilyPerson("Сергей", "Пупкин", "Пупкин", new GregorianCalendar(1950, 1, 20), "male");
        FamilyPerson lena = new FamilyPerson("Лена", "Пупкина", "Пупкина", new GregorianCalendar(2018, 10, 15), "female");
        FamilyPerson olya = new FamilyPerson("Оля", "Пупкина", "Пупкина", new GregorianCalendar(2020, 2, 25), "female");
        FamilyNode family2 = new FamilyNode(sergay, sergay);
        family2.setFamilyName("Пупкины 1");
        FamilyNode family1 = new FamilyNode(vasya, masha);
        family1.setFamilyName("Пупкины 2");
        family1.setChild(lena);
        family1.setChild(olya);
        family1.addHusbandParents(family2);

        System.out.print(IO.RED + "Семья 1: " + IO.RESET);
        family1.printInfo();
        System.out.print(IO.RED + "\n\nСемья 2:" + IO.RESET);
        family2.printInfo();
        System.out.printf("%s\n\nРодители: %s %s%s", IO.RED, lena.getName(), lena.getSurname(), IO.RESET);
        lena.printCouple(lena.getParents());
        System.out.printf("%s\n\nСвязи: %s %s%s", IO.RED, lena.getName(), lena.getSurname(), IO.RESET);
        lena.printResearchInfo(lena);

        System.out.printf("%s\n\nВосходящее древо: %s %s%s\n", IO.RED, lena.getName(), lena.getSurname(), IO.RESET);
        lena.printInfo();
        lena.ascendTree(lena.getParents());

    }
}
