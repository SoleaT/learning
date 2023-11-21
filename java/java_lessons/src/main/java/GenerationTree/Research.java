package GenerationTree;

//интерфейс исследований
public interface Research {


    //Исследование связей между двумя людьми
//    void twoPeopleRelations(FamilyPerson p1, FamilyPerson p2);

    //Исследование связей одного человека
    default void printResearchInfo(FamilyPerson p) {
        System.out.println(IO.CYAN + "\nИнформация: " + IO.RESET);
        p.printInfo();
        FamilyNode pp = p.getParents();
        if (pp != null) {
            System.out.print(IO.CYAN + "\nРодители:" + IO.RESET);
            pp.printCouple(pp);
            if (pp.getHusbParents() != null | pp.getWifeParents() != null) {
                System.out.print(IO.CYAN + "Бабушки и дедушки:" + IO.RESET);
                pp.printParents();
            }
        }
        if (p.getFamily() != null) {
            p.getFamily().printChildren();
        }
    }
}
