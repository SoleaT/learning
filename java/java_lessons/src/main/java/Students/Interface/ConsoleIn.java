package Students.Interface;

import Students.Model.*;

import java.util.*;

public class ConsoleIn implements Input {
    @Override
    public List<PersonalData> getPersonalData() {
        System.out.println("Создание студентов");
        List<PersonalData> students = new ArrayList<>();
        while (true) {
            System.out.println("Для выхода нажмите q, для заполнения данных - любую кнопку.");
            if (readStr().equals("q")) {
                break;
            }
            PersonalData newStudent = new PersonalData();
            System.out.print("Имя студента: ");
            newStudent.setName(readStr());
            System.out.print("Фамилия студента: ");
            newStudent.setSurname(readStr());
            System.out.print("Дата рождения в формате дд.мм.гггг: ");
            String[] temp = readStr().split("[.]");
            int[] datatemp = new int[3];
            for (int i = 0; i < 3; i++) {
                datatemp[i] = Integer.parseInt(temp[i]);
            }
            newStudent.setBirthDate(new GregorianCalendar(datatemp[0], datatemp[1], datatemp[2]));
            System.out.print("Телефон: ");
            newStudent.setPhone(readStr());
            System.out.print("Инн: ");
            newStudent.setInn(readStr());
            students.add(newStudent);
        }
        return students;
    }

    @Override
    public List<Group> getGroups() {
        System.out.println("Создание групп");
        List<Group> groups = new ArrayList<>();
        while (true) {
            System.out.println("Для выхода нажмите q, для заполнения данных - любую кнопку.");
            if (readStr().equals("q")) {
                break;
            }
            Group newGroup = new Group();
            System.out.print("Код группы: ");
            newGroup.setGroupNum(readStr());
            System.out.print("Факультет: ");
            newGroup.setFaculty(readStr());
            System.out.print("Год создания: ");
            newGroup.setYearOFEntry(Integer.parseInt(readStr()));
            System.out.print("Вид обучения: ");
            if (readStr().equalsIgnoreCase("очное")) {
                newGroup.setStudyType(StudyType.INTERNAL);
            } else {
                newGroup.setStudyType(StudyType.EXTERNAL);
            }
            groups.add(newGroup);
        }
        return groups;
    }

    @Override
    public List<StudentData> getStudents(List<PersonalData> students, List<Group> groups) {
        List<StudentData> matching = new ArrayList<>();
        Random r = new Random();
        for (PersonalData student : students) {
            matching.add(new StudentData(groups.get(r.nextInt(2)), student, StudyBase.values()[r.nextInt(4)]));
        }
        return matching;
    }


    public static String readStr() {
        Scanner readL = new Scanner(System.in);
        return readL.nextLine();
    }
}
