package GenerationTree;

import java.util.Calendar;

//Класс, описывающий одну персону в дереве
public class FamilyPerson extends Person implements IO, Research {

    private String gender;
    private FamilyNode parents;
    private FamilyNode family;

    public FamilyPerson(String name, String surname, String maidenName, Calendar dateOfBirth, String gender) {
        super(name, surname, maidenName, dateOfBirth);
        this.gender = gender;
    }

    public FamilyNode getFamily() {
        return family;
    }

    //Переменная заполняется при создании семьи в классе FamilyNode.
    public void setFamily(FamilyNode family) {
        this.family = family;
    }

    public String getGender() {
        return gender;
    }

    @Override
    //Метод для печати информации о человеке.
    public void printInfo() {
        String sex = getGender().equals("male") ? "мужчина" : "женщина";

        System.out.print(getName() + " " + getSurname() + ", " + sex + ", "
                + getDateOfBirth().get(Calendar.DAY_OF_MONTH) + "."
                + getDateOfBirth().get(Calendar.MONTH) + "."
                + getDateOfBirth().get(Calendar.YEAR));
    }

    public FamilyNode getParents() {
        return parents;
    }

    //Переменная заполняется при установке человека ребенком в классе FamilyNode.
    public void setParents(FamilyNode parents) {
        this.parents = parents;
    }

//    @Override
//    public void twoPeopleRelations(FamilyPerson p1, FamilyPerson p2) {
//        System.out.println("Еще не реализован");
//    }

}
