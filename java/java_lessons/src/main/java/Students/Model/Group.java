package Students.Model;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

//группы
@AllArgsConstructor
@NoArgsConstructor
@Getter
@Setter
public class Group {
    public String groupNum;
    protected String faculty;
    protected int yearOFEntry;
    protected StudyType studyType;

    @Override
    public String toString() {
        return "Группа " + groupNum +
                ", на факультете " + faculty +
                ", год поступления: " + yearOFEntry +
                ", тип обучения: " + studyType;
    }
}
