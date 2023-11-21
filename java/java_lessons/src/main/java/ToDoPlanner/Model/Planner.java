package ToDoPlanner.Model;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.util.Calendar;
import java.util.Date;

@Getter
@Setter
@NoArgsConstructor
public abstract class Planner {
    protected String taskName;
    protected String userName;
    protected Date deadline;
    protected Priority priority;
    protected Date start;
    protected int id;
    private static int numOfTasks=0;


    public Planner(String taskName, String userName, Date deadline) {
        this.taskName = taskName;
        this.userName = userName;
        this.deadline = deadline;
        this.setStart(Calendar.getInstance().getTime());
        this.setId(++numOfTasks);
    }

    @Override
    public String toString() {
        return String.format("Название задачи: %s с приоритетом %s, постановщик задачи: %s, " +
                "дедлайн %s", taskName, priority, userName, deadline.toString());
    }

}
