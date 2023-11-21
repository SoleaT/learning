//Задайте прямоугольный двумерный массив. Напишите программу, которая будет находить строку с наименьшей суммой элементов.

using learningLibrary;

var currentWork = new myLearningClass();

Console.Clear();

System.Console.Write("Введите количество строк: ");
int rowCount = currentWork.InputNumbers();
System.Console.Write("Введите количество столбцов: ");
int colCount = currentWork.InputNumbers();
int[,] intArray = new int[rowCount, colCount];
currentWork.FillRandomArray(intArray, 0, 10);
currentWork.PrintMatrix(intArray);
int sum = GetSummOfRow(intArray, 0);
int result = 0;

for (int i = 1; i < colCount; i++)
{
    int tempSum = GetSummOfRow(intArray, i);
    if (tempSum < sum)
    {
        result = i;
        sum = tempSum;
    }
}
System.Console.WriteLine($"Строка № {result+1}");

int GetSummOfRow(int[,] tempArray, int r)
{
    int rows = tempArray.GetLength(0);
    int sum = 0;
    for (int i = 0; i < rows; i++)
    {
        sum += tempArray[r, i];
    }
    return sum;
}