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
    for (int i = 0; i < rows; i++)
    {
        for (int q = 0; q < rows - i; q++)
            System.Console.Write("  ");
        for (int j = 0; j < rows; j++)
            if (tempArray[i, j] != 0) System.Console.Write("  {0:D} ", tempArray[i, j]);
        System.Console.WriteLine();
    }
}