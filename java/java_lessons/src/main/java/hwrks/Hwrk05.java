//package hwrks;
//
//import javafx.util.Pair;
//
//import java.util.ArrayList;
//
//import static hwrks.Stuff_hwrk.readStr;
//import static java.lang.System.exit;
//
//class Lab {
//    static int beginX;
//    static int beginY;
//    public static int[][] map;
//
//    public Lab(int[][] map) {
//        Lab.setMap(map);
//    }
//
//    public static void findStartCell() {
//        for (int i = 0; i < map.length; i++) {
//            for (int j = 0; j < map[0].length; j++) {
//                if (map[i][j] == -3) {
//                    beginY = j;
//                    beginX = i;
//                    return;
//                }
//            }
//        }
//        System.out.println("Не найдено начальной точки");
//        exit(1);
//    }
//
//
//    public static int[][] getMap() {
//        return map;
//    }
//
//    @Override
//    public String toString() {
//        StringBuilder xTemp = new StringBuilder();
//        for (int i = 0; i < getMap().length; i++) {
//            xTemp.append("\n");
//            for (int j = 0; j < getMap()[0].length; j++) {
//                if (i == beginX & j == beginY) {
//                    xTemp.append("\u001B[36m x \u001B[0m");
//                } else {
//                    if (map[i][j] == 0) {
//                        xTemp.append(" ░ ");
//                    } else if (map[i][j] == -1) {
//                        xTemp.append(" ▓ ");
//                    } else if (map[i][j] == -2) {
//                        xTemp.append("\u001B[31m ╳  \u001B[0m");
//                    } else if (map[i][j] == -5) {
//                        xTemp.append("\u001B[31m o \u001B[0m");
//                    } else {
//                        xTemp.append(String.format("%2d ", map[i][j]));
//                    }
//                }
//            }
//        }
//        return xTemp.toString();
//    }
//
//    public static void setMap(int[][] map) {
//        Lab.map = map;
//    }
//
//    public static void findPath(int yfin, int xfin) {
//        int x = xfin;
//        int y = yfin;
//        ArrayList<Pair<Integer, Integer>> path = new ArrayList<>();
//        int width = map.length;
//        int height = map[0].length;
//        int step = map[x][y];
//        do {
//            if (x < width - 1 && map[x + 1][y] == step - 1) {
//                path.add(new Pair<>(++x, y));
//            }
//            if (y < height - 1 && map[x][y + 1] == step - 1) {
//                path.add(new Pair<>(x, ++y));
//            }
//            if (x > 0 && map[x - 1][y] == step - 1) {
//                path.add(new Pair<>(--x, y));
//            }
//            if (y > 0 && map[x][y - 1] == step - 1) {
//                path.add(new Pair<>(x, --y));
//            }
//            step--;
//        } while (step != 0);
//        map[xfin][yfin] = -2;
//        for (Pair<Integer, Integer> pathItem : path) {
//            map[pathItem.getKey()][pathItem.getValue()] = -5;
//        }
//    }
//
//    public static void paintCells() {
//        ArrayList<Pair<Integer, Integer>> que = new ArrayList<>();
//        que.add(0, new Pair<>(beginX, beginY));
//        int step = 0;
//        map[beginX][beginY] = 0;
//        int width = map.length;
//        int height = map[0].length;
//        boolean finished = false;
//        while (que.size() > 0 && step < width * height && !finished) {
//            Pair<Integer, Integer> currentCell = que.remove(que.size() - 1);
//            int x = currentCell.getKey();
//            int y = currentCell.getValue();
//            if (map[x][y] == -2) finished = true;
//            step = map[x][y];
//            if (x < width - 1 && map[x + 1][y] == 0) {
//                que.add(new Pair<>(x + 1, y));
//                map[x + 1][y] = step + 1;
//            }
//            if (y < height - 1 && map[x][y + 1] == 0) {
//                que.add(new Pair<>(x, y + 1));
//                map[x][y + 1] = step + 1;
//            }
//            if (x > 0 && map[x - 1][y] == 0) {
//                que.add(new Pair<>(x - 1, y));
//                map[x - 1][y] = step + 1;
//            }
//            if (y > 0 && map[x][y - 1] == 0) {
//                que.add(new Pair<>(x, y - 1));
//                map[x][y - 1] = step + 1;
//            }
//        }
//    }
//}
//
//public class Hwrk05 {
//
//    static int[][] map = new int[][]{
//            {0, 0, 0, 0, 0, 0, 0, 0},
//            {0, 0, -1, 0, 0, 0, 0, 0},
//            {0, 0, -1, 0, -1, 0, -1, 0},
//            {0, -3, -1, 0, 0, 0, -1, 0},
//            {0, 0, -1, 0, 0, 0, -1, 0},
//            {0, -1, -1, -1, -1, -1, -1, 0},
//            {0, 0, -1, 0, 0, 0, -1, 0},
//            {0, 0, -1, 0, 0, 0, -1, 0},
//            {0, 0, 0, 0, 0, 0, -1, 0},
//            {0, 0, 0, 0, 0, 0, -1, 0},
//            {0, 0, 0, 0, 0, 0, 0, 0}
//    };
//
//
//    static int[] point = new int[2];
//
//
//    public static void main(String[] args) {
//
//        Lab newlab = new Lab(map);
//        newlab.findStartCell();
//        System.out.println(newlab);
//        System.out.println("До какой точки искать путь?");
//        try {
//            int i = 0;
//            for (String item : readStr().split(",")) {
//                point[i++] = Integer.parseInt(item);
//            }
//        } catch (Exception e) {
//            System.out.println("Не удалось прочитать " + e);
//        }
//
//        newlab.paintCells();
//        newlab.findPath(point[0] - 1, point[1] - 1);
//        System.out.println(newlab);
//    }
//}
