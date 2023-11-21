package Students.Interface;

import Students.Model.*;

import java.util.*;

public class DefIn implements Input {
    @Override
    public List<PersonalData> getPersonalData() {
        List<PersonalData> students = new ArrayList<>();
        students.add(new PersonalData("Вася", "Васильев", new GregorianCalendar(2000, 1, 1), "+79185555555", "12345678912"));
        students.add(new PersonalData("Джон", "Коннор", new GregorianCalendar(1980, 5, 10), "+119185555555", ""));
        students.add(new PersonalData("Алена", "Пупыщева", new GregorianCalendar(1990, 7, 2), "+79185555555", "8978451548451322"));
        students.add(new PersonalData("Екатерина", "Пупыщева", new GregorianCalendar(1995, 2, 12), "+79185555555", "548453255854333"));
        students.add(new PersonalData("Антон", "Афигеев", new GregorianCalendar(1995, 8, 21), "+79185555555", "548956413456"));
        return students;
    }

    @Override
    public List<Group> getGroups() {
        List<Group> groups = new ArrayList<>();
        groups.add(new Group(String.format("ABC-%s", Calendar.getInstance().get(Calendar.YEAR)), "Дураковаляние", Calendar.getInstance().get(Calendar.YEAR), StudyType.EXTERNAL));
        groups.add(new Group(String.format("CFR-%s", Calendar.getInstance().get(Calendar.YEAR) - 1), "Болтология", Calendar.getInstance().get(Calendar.YEAR)-1, StudyType.INTERNAL));
        return groups;
    }

    @Override
    public List<StudentData> getStudents(List<PersonalData> students, List<Group> groups) {
        List<StudentData> matching = new ArrayList<>();
        Random r = new Random();
        for (int i = 0; i < students.size(); i++) {
            matching.add(new StudentData(groups.get(r.nextInt(2)),students.get(i), StudyBase.values()[r.nextInt(4)]));
        }
        return matching;
    }

}
