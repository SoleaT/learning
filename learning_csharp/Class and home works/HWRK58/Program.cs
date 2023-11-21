//Задайте две матрицы. Напишите программу, которая будет находить произведение двух матриц.
using learningLibrary;

var currentWork = new myLearningClass();
Console.Clear();

System.Console.Write("Введите количество строк первой матрицы: ");
int rowCount = currentWork.InputNumbers();
System.Console.Write("Введите количество столбцов первой матрицы: ");
int colCount = currentWork.InputNumbers();


System.Console.Write("Введите количество строк второй матрицы: ");
int rowCount2 = currentWork.InputNumbers();
System.Console.Write("Введите количество столбцов второй матрицы: ");
int colCount2 = currentWork.InputNumbers();

if (colCount != rowCount2)
    System.Console.WriteLine("Умножение этих матриц невозможно");
else
{
    int[,] intArray = new int[rowCount, colCount];
    int[,] intArray2 = new int[rowCount2, colCount2];
    currentWork.FillRandomArray(intArray, 0, 5);
    System.Console.WriteLine("Первая матрица:");
    currentWork.PrintMatrix(intArray);
    currentWork.FillRandomArray(intArray2, 0, 5);
    System.Console.WriteLine("Вторая матрица:");
    currentWork.PrintMatrix(intArray2);
    System.Console.WriteLine("\nРезультат:");
    currentWork.PrintMatrix(MultiplyMatrix(intArray, intArray2));
}

int[,] MultiplyMatrix(int[,] array1, int[,] array2)
{
    int rows = array1.GetLength(0), cols = array2.GetLength(1);
    int count = array1.GetLength(1);
    int[,] tempArray = new int[rows, cols];
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            for (int k = 0; k < count; k++)
            {
                tempArray[i, j] += array1[i, k] * array2[k, j];
            }
        }
    }
    return tempArray;
}
