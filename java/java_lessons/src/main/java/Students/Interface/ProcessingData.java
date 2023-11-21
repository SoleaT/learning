package Students.Interface;

import Students.Model.Group;
import Students.Model.StudentData;

import java.util.ArrayList;
import java.util.List;

//этот интерфейс нужен, чтоб получать данные, которые потом выводятся пользователю
public interface ProcessingData {

    default List<StudentData> makeGroup(Group group, List<StudentData> studentsMatch) {
        List<StudentData> newList = new ArrayList<>();
        for (StudentData stu:studentsMatch) {
            if (stu.getGroupName()==group) {
                newList.add(stu);
            }
        }
        return newList;
    }
}
