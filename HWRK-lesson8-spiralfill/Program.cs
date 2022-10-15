//Напишите программу, которая заполнит спирально массив 4 на 4.

Console.Clear();

// int dim = 4; //условие задачи, с ним работает, так что сделала для любого размера
System.Console.WriteLine("Введите размерность матрицы: ");
int dim = int.Parse(Console.ReadLine()!);

int[,] spireArray = new int[dim, dim];
DoSpiralFill(spireArray);
PrintMatrix(spireArray);

void DoSpiralFill(int[,] spireArray)
{
    int rows = spireArray.GetLength(0);
    int cols = spireArray.GetLength(1);
    int j = 0, i = 0, k = 1;
    while (k < rows * cols)
    {
        while (j < cols & spireArray[i, j + 1] == 0)
        {
            spireArray[i, j] = k;
            j++;
            k++;
            if (j + 1 >= cols) break;
        }
        while (i < rows & spireArray[i + 1, j] == 0)
        {
            spireArray[i, j] = k;
            i++;
            k++;
            if (i + 1 >= rows) break;
        }
        while (j >= 0 & spireArray[i, j - 1] == 0)
        {
            spireArray[i, j] = k;
            j--;
            k++;
            if (j - 1 == -1) break;
        }
        while (i >= 0 & spireArray[i - 1, j] == 0)
        {
            spireArray[i, j] = k;
            i--;
            k++;
        }
        if (k == cols * rows) spireArray[i, j] = k;
    }
}

void PrintMatrix(int[,] tempArray)
{
    int rows = tempArray.GetLength(0);
    int cols = tempArray.GetLength(1);
    for (int i = 0; i < rows; i++)
    {
        System.Console.Write("[");
        for (int j = 0; j < cols; j++)
        {
            System.Console.Write("{0,3}", tempArray[i, j]);
        }
        System.Console.WriteLine("]");
    }
}