package GenerationTree;

import java.util.ArrayList;

//Основная конструкция для работы с генеалогическом древом.
public class FamilyNode implements IO {
    //В переменные записывается "название" семьи, супруги, родительские ноды и дети
    private String familyName;
    private FamilyPerson husband;
    private FamilyPerson wife;

    private FamilyNode husbParents;
    private FamilyNode wifeParents;
    public ArrayList<FamilyPerson> children = new ArrayList<>();

    public FamilyNode(FamilyPerson husband, FamilyPerson wife) {
        this.husband = husband;
        this.wife = wife;
        this.husband.setFamily(this);
        this.wife.setFamily(this);
    }

    public FamilyNode getHusbParents() {
        return husbParents;
    }

    public FamilyNode getWifeParents() {
        return wifeParents;
    }

    //Методы для установки родителей напрямую
    public void addWifeParents(FamilyNode f) {
        this.wifeParents = f;
        f.setChild(this.wife);
    }

    public void addHusbandParents(FamilyNode f) {
        this.husbParents = f;
        f.setChild(this.husband);
    }

    @Override
    //Вывод информации о семье: супруги, родители, дети
    public void printInfo() {
        System.out.printf("%s\n______________\nСемья: %s%s", IO.GREEN, this.familyName, IO.RESET);
        printCouple(this);
        printChildren();
        printParents();
    }

    //Вывод списка детей
    public void printChildren() {
        if (children.size() > 0) {
            System.out.print(IO.YELLOW + "Дети:" + IO.RESET);
            for (FamilyPerson child : children) {
                System.out.print("\nРебенок ");
                child.printInfo();
            }
        }
    }

    //Метод для печати родителей супругой
    public void printParents() {
        if (this.husbParents != null) {
            System.out.print(IO.YELLOW + "\nРодители мужа: " + IO.RESET);
            this.husbParents.getHusband().printInfo();
            System.out.print(", ");
            this.husbParents.getWife().printInfo();
        }
        if (this.wifeParents != null) {
            System.out.print(IO.YELLOW + "\nРодители жены: " + IO.RESET);
            this.wifeParents.getHusband().printInfo();
            System.out.print(", ");
            this.wifeParents.getWife().printInfo();
        }
    }

    public FamilyPerson getHusband() {
        return husband;
    }

    public FamilyPerson getWife() {
        return wife;
    }

    //Внесение в список детей, при этом у детей автоматически выставляются ссылки на родительский нод
    public void setChild(FamilyPerson child) {
        this.children.add(child);
        child.setParents(this);
    }

    public String getFamilyName() {
        return familyName;
    }

    public void setFamilyName(String familyName) {
        this.familyName = familyName;
    }
}
