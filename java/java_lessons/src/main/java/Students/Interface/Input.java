package Students.Interface;

import Students.Model.Group;
import Students.Model.PersonalData;
import Students.Model.StudentData;

import java.util.List;

public interface Input {
    List<PersonalData> getPersonalData();
    List<Group> getGroups();
    List<StudentData> getStudents(List<PersonalData> students, List<Group> groups);
}
