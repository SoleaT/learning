Console.Clear();

System.Console.Write("Введите количество строк: ");
int rowCount = int.Parse(Console.ReadLine());
System.Console.Write("Введите количество столбцов: ");
int colCount = int.Parse(Console.ReadLine());
int[,] intArray = new int[rowCount, colCount];

FillRandomArray(intArray, -10, 20);
PrintMatrix(intArray);

var position = FindMinPositions(intArray);

int[,] newArray = new int[rowCount - 1, colCount - 1];

int k = 0, l = 0;

for (int i = 0; i < rowCount; i++)
{
    l = 0;
    if (i == position.x) continue;
    for (int j = 0; j < colCount; j++)
    {
        if (j == position.y) continue;

        newArray[k, l] = intArray[i, j];
        l++;
    }
    k++;
}
PrintMatrix(newArray);

(int x, int y) FindMinPositions(int[,] tempArray)
{
    int min = tempArray[0, 0], xpos = 0, ypos = 0;
    for (int i = 0; i < tempArray.GetLength(0); i++)
    {
        for (int j = 0; j < tempArray.GetLength(1); j++)
        {
            if (tempArray[i, j] < min)
            {
                min = tempArray[i, j];
                xpos = i;
                ypos = j;
            }
        }
    }
    return (xpos, ypos);
}

// PrintMatrix(intArray);
// if (colCount != rowCount)
// {
//     System.Console.WriteLine("Невозможно копировать");
// }
// else
// {
//     FillRandomArray(intArray, 1, 10);
//     int[,] newArray = new int[rowCount, colCount];
//     for (int i = 0; i < rowCount; i++)
//     {
//         for (int j = 0; j < colCount; j++)
//         {
//             newArray[j, i] = intArray[i, j];
//         }
//     }
//     System.Console.WriteLine("Исходный массив");
//     PrintMatrix(intArray);
//     System.Console.WriteLine("Полученный массив");
//     PrintMatrix(newArray);
// }

void FillRandomArray(int[,] tempArray, int firstNum, int secondNum)
{
    int rows = tempArray.GetLength(0);
    int cols = tempArray.GetLength(1);
    var r = new Random();
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            tempArray[i, j] = r.Next(firstNum, secondNum);
        }
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