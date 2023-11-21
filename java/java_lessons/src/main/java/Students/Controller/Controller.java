package Students.Controller;

import Students.Interface.ConsoleIn;
import Students.Interface.ConsoleOut;
import Students.Interface.DefIn;
import Students.Model.Group;
import Students.Model.PersonalData;
import Students.Model.StudentData;

import java.util.Collections;
import java.util.List;

public class Controller {
    public void start() {
        List<PersonalData> students = new DefIn().getPersonalData();
        List<Group> groups = new DefIn().getGroups();
        List<StudentData> matchGroups= new DefIn().getStudents(students,groups);

        List<PersonalData> students2 = new ConsoleIn().getPersonalData();

        //создаем вывод в консольку
        ConsoleOut console=new ConsoleOut();

        //список студентов по группам
        for (Group gr:groups) {
            console.viewGroup(gr,matchGroups);
        }

        //список групп
        console.viewGroupsList(groups);

        //общий список студентов без разделения на группы
        console.viewStudentsData(matchGroups);

        //список персональных данных студентов
        console.viewFullList(students);

        //инфо одного студента
        console.viewPersonalInfo(students.get(1));

        //вывод после сортировки
        Collections.sort(students);
        console.viewFullList(students);
    }
}
