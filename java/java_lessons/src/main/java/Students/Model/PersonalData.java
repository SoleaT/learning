package Students.Model;

import lombok.Getter;
import lombok.Setter;
import org.jetbrains.annotations.NotNull;

import java.util.Calendar;

//личные данные студентов
@Getter
@Setter
public class PersonalData implements Comparable<PersonalData> {
    protected int id;
    protected String name;
    protected String surname;
    protected Calendar birthDate;
    protected String phone;
    protected String inn;
    private static int idIncrement=0;

    public PersonalData(){
        this.setId(idIncrement++);
    }
    public PersonalData(String name, String surname, Calendar birthDate, String phone, String inn) {
        this.name = name;
        this.surname = surname;
        this.birthDate = birthDate;
        this.phone = phone;
        if (inn.length()>11) {
            inn=inn.substring(0,11);
        }
        this.inn = inn;
        this.setId(idIncrement++);
    }

    @Override
    public String toString() {
        return "Персональные данные студента:" +
                "\n\t id=" + id +
                "\n\t имя: " + name +
                "\n\t фамилия: " + surname +
                "\n\t дата рождения: " + birthDate.getTime() +
                "\n\t телефон: " + phone +
                "\n\t ИНН: " + inn +
                "\n_________";
    }

    @Override
    public int compareTo(@NotNull PersonalData o) {
        return o.getBirthDate().compareTo(this.getBirthDate());
    }
}
