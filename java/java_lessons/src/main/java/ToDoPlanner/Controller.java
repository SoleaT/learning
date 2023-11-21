package ToDoPlanner;

import ToDoPlanner.Model.*;
import ToDoPlanner.Model.Queue;
import ToDoPlanner.View.ExportInfo;

import java.util.*;

public class Controller implements ExportInfo {
    public static void start() {
        int numberOfTasks=10;
        Random rand = new Random();
        Planner task;
        Queue<Planner> qw = new Queue<>();
        for (int i = 0; i < numberOfTasks; i++) {
            Calendar date1 = new GregorianCalendar(2023,rand.nextInt(2,11), rand.nextInt(1,25));
            int r = rand.nextInt(3);
            switch (r) {
                case 0 -> {
                    task = new HighPrioTask("Task" + i, "user1", date1.getTime());
                    qw.setQueue(task);
                }
                case 1 -> {
                    task = new MidPrioTask("Task" + i, "user1", date1.getTime());
                    qw.setQueue(task);
                }
                case 2 -> {
                    task = new LowPrioTask("Task" + i, "user1", date1.getTime());
                    qw.setQueue(task);
                }
            }
        }
        System.out.printf("Установлено %s задач. Выполняем, ожидайте\n",Queue.tasksNumber);
        ExportInfo.writeToFile(qw);
    }
}
