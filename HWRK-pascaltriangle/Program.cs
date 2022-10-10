using System.Linq;

Console.Clear();

System.Console.WriteLine("Сколько строк треугольника вывести?");
int n = Convert.ToInt32(Console.ReadLine());
int[,] pascalArray = new int[n, n];
for (int i = 0; i < n; i++)
{
    for (int j = 0; j < n; j++)
    {
        if (j == i | j == 0)
            pascalArray[i, j] = 1;
        else if (j > i)
            pascalArray[i, j] = 0;
        else
            pascalArray[i, j] = pascalArray[i - 1, j - 1] + pascalArray[i - 1, j];
    }
}
PrintMatrix(pascalArray);


void PrintMatrix(int[,] tempArray)
{
    int rows = tempArray.GetLength(0);
    int cols = tempArray.GetLength(1);
    int cursorPos;
    for (int i = 0; i < rows; i++)
    {
        cursorPos = Console.WindowWidth / 2 - i;
        Console.SetCursorPosition(cursorPos, Console.CursorTop);
        for (int j = 0; j < cols; j++)
        {
            if (tempArray[i, j] != 0) System.Console.Write($"{tempArray[i, j]} ");
        }
        System.Console.WriteLine();
    }
}