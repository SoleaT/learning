package hwrks;

import java.io.File;
import java.io.FileWriter;

public class Hwrk02_2 {
    public static void main(String[] args) {
        String filename = "hwrk2_1.txt";
        String whatToWrite = "TEST";
        int count = 100;

        //проверка файла
        String path = System.getProperty("user.dir").concat("/" + filename);
        File tempFile = new File(path);
        if (tempFile.exists()) {
            if (tempFile.canWrite()) {
                System.out.println("Файл найден и может быть отредактирован.");
            } else {
                System.out.println("Файл найден, но к нему нет доступа.");
                System.exit(0);
            }
        } else {
            System.out.println("Файл не найден и будет создан.");
            try {
                if (tempFile.createNewFile()) {
                    System.out.println("Создан новый файл.");
                }
            } catch (Exception e) {
                System.out.printf("Возникла ошибка: %s", e);
                System.exit(0);
            }
        }

        //запись в файл
        writeToFile(
                path,
                formStringForFile(whatToWrite,count)
        );
    }

    private static String formStringForFile(String tempStr, int count) {
        return tempStr.repeat(count);
    }

    private static void writeToFile(String path, String whatToWrite) {
        try (FileWriter writeText = new FileWriter(path, false)) {
            writeText.write(whatToWrite);
            writeText.flush();
            System.out.println("Данные записаны в файл");
        } catch (Exception e) {
            System.out.printf("Да всё ж уже проверили, но вот те на,  всё равно ошибка: %s",e);
        }
    }
}
