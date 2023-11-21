package Students.Model;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

//класс, соединяющий студентов и группы
@AllArgsConstructor
@NoArgsConstructor
@Getter
@Setter
public class StudentData {
    protected Group groupName;
    protected PersonalData studentName;
    protected StudyBase typeOfStudy;

    @Override
    public String toString() {
        return "Студент:" +
                " по имени " + getStudentName().getName() + " " + getStudentName().getSurname() +
                " находится в группе " + getGroupName().getGroupNum() +
                " с типом обучения " + getTypeOfStudy();
    }
}
