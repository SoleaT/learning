package org.example;

import java.util.*;

public class exl01 {

    public static final String reset = "\u001B[0m";
    public static final String red = "\u001B[31m";
    public static final String yellow = "\u001B[33m";
    public static final String cyan = "\u001B[36m";
    public static Random rand = new Random();

    private static int userInput(String msg) {
        Scanner sc = new Scanner(System.in);
        int inputStr;
        while (true) {
            System.out.print(msg);
            try {
                inputStr = Integer.parseInt(sc.next());
                break;
            } catch (NumberFormatException e) {
                System.out.println(red + "Неверный ввод! Введите целое число!" + reset);
            }
        }
        return inputStr;
    }
    public static void main(String[] args) {
        List<String> planets = List.of("Меркурий", "Венера", "Земля", "Марс", "Юпитер", "Сатурн", "Уран", "Нептун");
        System.out.println(planets);
        int arrSize = 20;
        ArrayList<String> newArr = new ArrayList<>();

        for (int i = 0; i < arrSize + 1; i++) {
            newArr.add(planets.get(rand.nextInt(planets.size())));
        }
        System.out.println(newArr);
        int counter;
        for (String planet : planets) {
            counter = Collections.frequency(newArr, planet);
            System.out.println(planet + counter);
        }


        Set<String> newSet = new HashSet<>(newArr);
        System.out.println(newSet);


    }
}

