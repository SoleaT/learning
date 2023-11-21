using learningLibrary;

myLearningClass currentWork = new myLearningClass();

bool wantToContinue = true;
while (wantToContinue)
{
    //какую задачу хотим решить
    Console.Clear();
    Console.WriteLine(@"Есть 4 задачи на выбор.
                        Задача 1: Задайте двумерный массив размером m×n, заполненный случайными вещественными числами.
                        Задача 2: Напишите программу, которая на вход принимает позиции элемента в двумерном массиве, и 
                        возвращает значение этого элемента или же указание, что такого элемента нет.
                        Задача 3: Задайте двумерный массив из целых чисел. Найдите среднее арифметическое элементов в каждом столбце.
                        Задача 4: Задайте двумерный массив из целых чисел. Определите, есть столбец в массиве, сумма которого, больше 
                        суммы элементов расположенных в четырех ""углах"" двумерного массива.");

    System.Console.WriteLine("Выберите номер задачи (1 2 3 4): ");
    int numOfWork = currentWork.InputNumbers();
    Console.Clear();
    char[] separators = { ' ', ',', ';' };
    System.Console.Write("Введите количество строк: ");
    int rowCount = currentWork.InputNumbers();
    System.Console.Write("Введите количество столбцов: ");
    int colCount = currentWork.InputNumbers();
    int[,] intArray = new int[rowCount, colCount];
    currentWork.FillRandomArray(intArray, 1, 10);
    switch (numOfWork) //разбор по задачам
    {
        case 1:
            double[,] doubleArray = new double[rowCount, colCount];
            currentWork.FillRandomArray(doubleArray, 0.0, 99.9);
            currentWork.PrintMatrix(doubleArray);
            break;
        case 2:
            currentWork.PrintMatrix(intArray);
            int[] elementPosition = new int[2];
            while (true)
            {
                System.Console.WriteLine("Введите позицию элемента (2 числа): ");
                elementPosition = Console.ReadLine()!.Split(separators).Select(int.Parse).ToArray();
                if (elementPosition.Length >= 2) break;
                System.Console.WriteLine("Нужно ввести 2 цифры");
            }
            if (elementPosition[0] >= rowCount || elementPosition[1] >= colCount)
            {
                System.Console.WriteLine("Номер позиции выходит за границы массива.");
                break;
            }
            System.Console.WriteLine($"Элемент на позиции [{elementPosition[0]},{elementPosition[1]}] = {intArray.GetValue(elementPosition)}");
            break;
        case 3:
            currentWork.PrintMatrix(intArray);
            for (int i = 0; i < colCount; i++)
            {
                System.Console.WriteLine($"Среднее арифметическое столбца {i}: {Math.Round(GetAverage(intArray[0, i], 0, i, intArray), 2)}");
            }
            break;
        case 4:
            int summ = intArray[0, 0]
                     + intArray[rowCount - 1, 0]
                     + intArray[0, colCount - 1]
                     + intArray[rowCount - 1, colCount - 1];
            currentWork.PrintMatrix(intArray);
            bool isColExists = false;
            int k = 0;
            int summTemp = 0;
            while (!isColExists & k < colCount)
            {
                summTemp = 0;
                for (int j = 0; j < rowCount; j++)
                    summTemp += intArray[j,k];
                if (summTemp > summ)
                    isColExists = true;
                k++;
            }
            if (isColExists)
                System.Console.WriteLine($@"Такой столбец найден - столбец #{k}
Сумма столбца {summTemp}, сумма элементов {summ}");
            else
                System.Console.WriteLine("Такой столбец не найден");
            break;
        default:
            Console.WriteLine("Такую задачу ещё не решали. Выбирайте цифру с умом.");
            break;
    }
    Console.Write("Хотите решить ещё задачу? (y/n)}");
    switch (Console.ReadKey(true).KeyChar.ToString().ToLower())
    {
        case "y":
            wantToContinue = true;
            Console.WriteLine();
            break;
        case "n":
            Console.WriteLine("\nСпасибо за использование программы. Пока!");
            wantToContinue = false;
            break;
        default:
            Console.WriteLine("\nКто разрешал жать любую клавишу?! Вот и иди теперь отсюда");
            wantToContinue = false;
            break;
    }
}

//рекурсия может и не нужна, но я ж их не понимаю, надо тренироваться
double GetAverage(double summ, int count, int col, int[,] tempArray)
{
    if (count == tempArray.GetLength(0) - 1)
    {
        return summ / (count + 1);
    }
    return GetAverage(summ + tempArray[count + 1, col], count + 1, col, tempArray);
}