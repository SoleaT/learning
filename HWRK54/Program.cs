// Задайте двумерный массив. Напишите программу, которая упорядочит по убыванию элементы каждой строки двумерного массива.

using learningLibrary;

var currentWork = new myLearningClass();

System.Console.Write("Введите количество строк: ");
int rowCount = currentWork.InputNumbers();
System.Console.Write("Введите количество столбцов: ");
int colCount = currentWork.InputNumbers();
int[,] intArray = new int[rowCount, colCount];
currentWork.FillRandomArray(intArray, 0, 10);
currentWork.PrintMatrix(intArray);


//сортировка строк
for (int i = 0; i < rowCount; i++)
    for (int j = colCount-1; j >=0; j--)
        for (int k = 1; k <= j; k++)
            if (intArray[i,k]>intArray[i,k-1])
                (intArray[i,k-1], intArray[i,k]) = (intArray[i,k], intArray[i,k-1]);
            

// сортировка столбцов
// for (int i = 0; i < colCount; i++)
//     for (int j = rowCount - 1; j >= 0; j--)
//         for (int k = 1; k <= j; k++)
//             if (intArray[k, i] > intArray[k - 1, i])
//                 (intArray[k - 1, i], intArray[k, i]) = (intArray[k, i], intArray[k - 1, i]);


System.Console.WriteLine();
currentWork.PrintMatrix(intArray);