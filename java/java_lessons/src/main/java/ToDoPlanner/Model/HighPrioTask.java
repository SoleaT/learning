package ToDoPlanner.Model;

import java.util.Date;

public class HighPrioTask extends Planner {

    protected Priority priority;

    public HighPrioTask(String taskName, String userName, Date deadline) {
        super(taskName, userName, deadline);
        this.setPriority(Priority.HIGH);
    }

    @Override
    public String toString() {
        return String.format("""
                Задача высокого уровня: %s
                _______""", super.toString());
    }
}
