package Students.Interface;

import Students.Model.Group;
import Students.Model.PersonalData;
import Students.Model.StudentData;

import java.util.List;

//это интерфейс для вывода в консоль
public class ConsoleOut implements Output,ProcessingData{

    @Override
    public void viewFullList(List<PersonalData> students) {
        for (PersonalData stud:students) {
            System.out.println(stud);
        }
    }

    @Override
    public void viewPersonalInfo(PersonalData student) {
        System.out.println(student);
    }

    @Override
    public void viewGroupsList(List<Group> groups) {
        System.out.println("Список групп");
        for (Group gr:groups) {
            System.out.println(gr);
        }
        System.out.println("________________");
    }

    @Override
    public void viewGroup(Group group, List<StudentData> studentsMatch) {
        List<StudentData> newList = makeGroup(group,studentsMatch);
        System.out.printf("Группа %s\n",group.groupNum);
        for (StudentData student:newList) {
            System.out.println(student);
        }
        System.out.println("________________");
    }

    @Override
    public void viewStudentsData(List<StudentData> studentsMatch) {
        System.out.println("Общий список студентов");
        for (StudentData student:studentsMatch) {
            System.out.println(student);
        }
        System.out.println("________________");
    }
}
