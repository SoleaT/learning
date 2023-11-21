package GenerationTree;

import java.util.Calendar;

public abstract class Person {
    private String name;
    private String surname;
    private String maidenName;
    private Calendar dateOfBirth;

    public Person(String name, String surname, String maidenName, Calendar dateOfBirth) {
        this.name = name;
        this.surname = surname;
        this.maidenName = maidenName;
        this.dateOfBirth = dateOfBirth;
    }

    protected Person() {
    }

    public String getName() {
        return name;
    }

    public String getSurname() {
        return surname;
    }

    public String getMaidenName() {
        return maidenName;
    }

    public Calendar getDateOfBirth() {
        return dateOfBirth;
    }
}
