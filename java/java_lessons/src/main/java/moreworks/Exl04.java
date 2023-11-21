package moreworks;

import java.util.Arrays;

public class Exl04 {
    public static void main(String[] args) {
        int bound = 1000;

        boolean[] primeNumbers= new boolean[bound];
        Arrays.fill(primeNumbers,true);
        primeNumbers[1]=false;
        for (int i = 2; i*i < bound ; i++) {
            if (primeNumbers[i]) {
                for (int j = i*i; j < bound; j+=i) {
                    primeNumbers[j] = false;
                }
            }
        }

        for (int i = 0; i <bound; i++) {
            if (primeNumbers[i]) {
                System.out.printf("%s ",i);
            }
        }
    }
}
