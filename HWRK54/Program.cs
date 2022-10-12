// Задайте двумерный массив. Напишите программу, которая упорядочит по убыванию элементы каждой строки двумерного массива.

using learningLibrary;

var currentWork = new myLearningClass();

System.Console.Write("Введите количество строк: ");
int rowCount = currentWork.InputNumbers();
System.Console.Write("Введите количество столбцов: ");
int colCount = currentWork.InputNumbers();
int[,] intArray = new int[rowCount, colCount];
currentWork.FillRandomArray(intArray, -10, 10);
currentWork.PrintMatrix(intArray);

for (int i = 0; i < colCount; i++)
{
    for (int j = rowCount - 1; j >= 0; j--)
    {
        //  System.Console.WriteLine($"j={j},i={i}");
        for (int k = 1; k <= j; k++)
        {
            
            if (intArray[k, i] > intArray[k - 1, i])
                (intArray[k - 1, i], intArray[k, i]) = (intArray[k, i], intArray[k - 1, i]);
        }
    }
}
System.Console.WriteLine();
currentWork.PrintMatrix(intArray);