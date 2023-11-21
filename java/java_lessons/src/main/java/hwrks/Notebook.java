package hwrks;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
public class Notebook {
    public String model;
    public String color;
    public int memory;
    public String proc;
    public int diag;

    @Override
    public String toString() {
        return "Ноутбук " +
                "модели " + model +
                ", цвет " + color +
                ", ОЗУ " + memory +
                "гб, процессор " + proc  +
                ", диагональ " + diag +
                "''";
    }

    public void nbSort() {

    }

}
