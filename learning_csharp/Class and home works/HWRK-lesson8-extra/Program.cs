//Сформируйте трёхмерный массив из неповторяющихся двузначных чисел. 
//Напишите программу, которая будет построчно выводить массив, добавляя индексы каждого элемента.
Console.Clear();

System.Console.Write("Введите размерность первого измерения: ");
int xCount = int.Parse(Console.ReadLine()!);
System.Console.Write("Введите размерность второго измерения: ");
int yCount = int.Parse(Console.ReadLine()!);
System.Console.Write("Введите размерность третьего измерения: ");
int zCount = int.Parse(Console.ReadLine()!);

if (xCount * yCount * zCount >= 100)
    System.Console.WriteLine("Для такого массива невозможно заполнение уникальными двузначными числами");
else
{
    int[,,] matrix3D = Fill3DMatrix(xCount, yCount, zCount);
    Print3DMatrix(matrix3D);
}

int[,,] Fill3DMatrix(int x, int y, int z)
{
    int[,,] tempArray = new int[x, y, x];
    var r = new Random();
    int newDig = r.Next(10, 100);
    for (int i = 0; i < x; i++)
        for (int j = 0; j < y; j++)
            for (int k = 0; k < z; k++)
            {
                while (isDigitExists(tempArray, newDig))
                {
                    newDig = r.Next(10, 100);
                }
                tempArray[i, j, k] = newDig;
            }
    return tempArray;
}

bool isDigitExists(int[,,] tempArray, int digit)
{
    foreach (int currentDigit in tempArray)
    {
        if (currentDigit == digit)
        {
            return true;
        }
    }
    return false;
}

void Print3DMatrix(int[,,] tempArray)
{
    int x = tempArray.GetLength(0);
    int y = tempArray.GetLength(1);
    int z = tempArray.GetLength(2);
    for (int i = 0; i < x; i++)
    {
        for (int j = 0; j < y; j++)
        {
            System.Console.WriteLine();
            for (int k = 0; k < z; k++)
            {
                System.Console.Write("{0,4}", tempArray[i, j, k]);
                System.Console.Write($"({i},{j},{k})");
            }
        }
    }
}