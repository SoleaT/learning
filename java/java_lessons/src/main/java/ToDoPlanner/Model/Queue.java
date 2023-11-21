package ToDoPlanner.Model;

import lombok.Getter;

import java.util.LinkedList;

@Getter
public class Queue<T extends Planner> {
    public LinkedList<T> highQ = new LinkedList<>();
    public LinkedList<T> midQ = new LinkedList<>();
    public LinkedList<T> lowQ = new LinkedList<>();
    public static int tasksNumber=0;

    public void setQueue(T task) {
        switch (task.getPriority()) {
            case LOW -> lowQ.add(task);
            case MID -> midQ.add(task);
            case HIGH -> highQ.add(task);
        }
        tasksNumber++;
    }

    public T leaveQueue(LinkedList<T> q) {
        tasksNumber--;
        return q.pop();
    }
}
