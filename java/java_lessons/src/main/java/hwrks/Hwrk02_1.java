package hwrks;


import static hwrks.Stuff_hwrk.readStr;

public class Hwrk02_1 {
    public static void main(String[] args) {
        System.out.print("Введите строку: ");
        char[] inputStr = readStr().
                toLowerCase().
                toCharArray();
        if (isPalindrome(inputStr)) {
            System.out.println("Строка является палиндромом");
        } else {
            System.out.println("Строка не является палиндромом");
        }
    }

    private static boolean isPalindrome(char[] tempstr) {
        boolean flag = true;
        for (int i = 0; i < (tempstr.length - 1) / 2; i++) {
            if (tempstr[i] != tempstr[tempstr.length - 1 - i]) {
                flag = false;
                break; //я протестую против этого решения. а идея говорит, что так надо. кто прав?
            }
        }
        return flag;
    }
}
