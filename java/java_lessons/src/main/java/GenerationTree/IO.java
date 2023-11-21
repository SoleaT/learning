package GenerationTree;

public interface IO {
    //интерфейс для вывода на экран
    String RESET = "\u001B[0m";
    String RED = "\033[91m";
    String YELLOW = "\033[93m";
    String CYAN = "\u001B[36m";
    String GREEN = "\033[92m";
    String BLUE = "\u001B[34m";
    String PURPLE = "\u001B[35m";


    void printInfo();

    default void printCouple(FamilyNode fn) {
        System.out.print(IO.YELLOW + "\nМуж: " + IO.RESET);
        fn.getHusband().printInfo();
        System.out.print(IO.YELLOW + "\nЖена: " + IO.RESET);
        fn.getWife().printInfo();
        System.out.printf(", в девичестве %s%n", fn.getWife().getMaidenName());
    }

    default void ascendTree(FamilyNode family) {
        printCouple(family);
        if (family.getHusbParents() != null) {
            System.out.println("\nРодители мужа:");
            ascendTree(family.getHusbParents());
        }
        if (family.getWifeParents() != null) {
            System.out.println("\nРодители жены:");
            ascendTree(family.getWifeParents());
        }

    }
}
