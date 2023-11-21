package Students.Interface;

import Students.Model.Group;
import Students.Model.PersonalData;
import Students.Model.StudentData;

import java.util.List;

//общий интерфейс для разных способов вывода данных
public interface Output {
    void viewFullList(List<PersonalData> students);
    void viewPersonalInfo(PersonalData student);
    void viewGroupsList(List<Group> groups);
    void viewGroup(Group group, List<StudentData> studentsMatch);
    void viewStudentsData(List<StudentData> studentsMatch);
}
