// Напишите программу, которая выводит монотонную последовательность из N элементов в виде равностороннего треугольника с помощью рекурсии

Console.Clear();
System.Console.Write("Введите N: ");
int n = int.Parse(Console.ReadLine() ?? "5");
PrintTriangle(n, 1, 1);

void PrintTriangle(int n, int rows, int col)
{
    if (rows - 1 == n) return;
    if (col == 1)
        for (int q = 0; q < n - rows; q++)
            System.Console.Write(" ");
    Console.Write(rows + " ");
    if (col == rows)
    {
        System.Console.WriteLine();
        col = 1;
        rows++;
    }
    else col++;
    PrintTriangle(n, rows, col);
}