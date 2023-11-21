package ToDoPlanner.Model;

import java.util.Date;

public class LowPrioTask extends Planner {

    protected Priority priority;

    public LowPrioTask(String taskName, String userName, Date deadline) {
        super(taskName, userName, deadline);
        this.setPriority(Priority.LOW);
    }


    @Override
    public String toString() {
        return String.format("""
                Задача низкого уровня: %s
                _______""", super.toString());
    }
}
