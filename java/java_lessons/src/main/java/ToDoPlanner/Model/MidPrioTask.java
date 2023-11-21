package ToDoPlanner.Model;

import java.util.Date;

public class MidPrioTask extends Planner {

    protected Priority priority;

    public MidPrioTask(String taskName, String userName, Date deadline) {
        super(taskName, userName, deadline);
        this.setPriority(Priority.MID);
    }

    @Override
    public String toString() {
        return String.format("""
                Задача среднего уровня: %s
                _______""", super.toString());
    }
}
