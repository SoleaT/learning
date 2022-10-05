using learningLibrary;

myLearningClass currentwork = new myLearningClass();

bool wanttocontinue = true;
while (wanttocontinue)
{
    //какую задачу хотим решить
    Console.Clear();
    Console.WriteLine(@"Есть 5 задач на выбор.
                        Задача 1: Задайте массив заполненный случайными положительными трёхзначными числами. Напишите программу, 
                        которая покажет количество чётных чисел в массиве.
                        Задача 2: Задайте одномерный массив, заполненный случайными числами. Найдите сумму элементов, стоящих на нечётных позициях.
                        Задача 3: Задайте массив вещественных чисел. Найдите разницу между максимальным и минимальным элементов массива.
                        Задача 4: Задайте одномерный массив, заполненный случайными числами. Из входного массива сформируйте массив с чётными 
                        и массив с нечётными значениями элементов входного массива. Найдите ср. арифметическое из полученных значений 
                        элементов массивов и выведите результат сравнения средних арифметических.
                        Задача 5: Задайте одномерный массив из N элементов, заполненный случайными числами. Необходимо определить, в какой 
                        последовательности заданы элементы массива: по возрастанию, по убыванию, хаотично, или все элементы одинаковы.");

    System.Console.WriteLine("Выберите номер задачи (1 2 3 4 5): ");
    int numofwork = currentwork.InputNumbers();
    int size = new Random().Next(10, 30); 
    int[] arrayint=new int[size];
    switch (numofwork) //разбор по задачам
    {
        case 1:
            arrayint = currentwork.FillRandomArray(size, 100, 1000);
            System.Console.WriteLine("Количество чётных элементов в массиве " + string.Join("|", arrayint) + " равно " + currentwork.CountEvenNumbers(arrayint));
            break;
        case 2:
            arrayint = currentwork.FillRandomArray(size, 0, 100);
            System.Console.WriteLine("Сумма элементов на нечётных позициях в массиве " + string.Join("|", arrayint) + " равно " + currentwork.CountSumOnEvenPositions(arrayint));
            break;
        case 3:
            double[] array1 = currentwork.FillRandomArray(size, 0.0, 50.0);
            double maxnumber =array1.Max(), minumber = array1.Min();
            System.Console.WriteLine($"Разница между максимальным {Math.Round(maxnumber, 2)} и минимальным {Math.Round(minumber, 2)} равна {Math.Round(maxnumber - minumber, 2)}");
            break;
        case 4:
            arrayint = currentwork.FillRandomArray(size, 0, 100);
            double evensum = currentwork.GetAverageFromArray(currentwork.MakeEvenOddArrays(arrayint).evenarray);
            double oddsum = currentwork.GetAverageFromArray(currentwork.MakeEvenOddArrays(arrayint).oddarray);
            if (evensum > oddsum)
                System.Console.WriteLine("средн. арифм. значений элементов массива с чётными числами > средн. арифм. значений элементов с нечётными числами");
            else if (oddsum > evensum)
                System.Console.WriteLine("средн. арифм. массива значений элементов с нечётными числами > средн. арифм. значений элементов с чётными числами");
            else
                System.Console.WriteLine("средн. арифм. значений элементов массива с нечётными числами = средн. арифм. значений элементов с чётными числами");
            break;
        case 5:
            System.Console.Write("Задайте размерность массива N: ");
            size = currentwork.InputNumbers();
            arrayint=currentwork.FillRandomArray(size,0,10);
            bool ifMax = false, ifMin = false;
            System.Console.WriteLine("Массив: "+string.Join(" ", arrayint));
            for (int i = 1; i < size; i++)
            {
                if (arrayint[i] > arrayint[i - 1]) ifMax = true;
                if (arrayint[i] < arrayint[i - 1]) ifMin = true;
            }
            if (ifMax && ifMin) System.Console.WriteLine("Элементы расположены хаотично");
            else if (!ifMax && !ifMin) System.Console.WriteLine("Элементы равны");
            else if (!ifMax && ifMin) System.Console.WriteLine("Элементы рассортированы по убыванию");
            else System.Console.WriteLine("Элементы рассортированы по возрастанию");
            break;
        default:
            Console.WriteLine("Такую задачу ещё не решали. Выбирайте цифру с умом.");
            break;
    }
    Console.Write("Хотите решить ещё задачу? (y/n)}");
    Console.WriteLine();
    switch (Console.ReadKey(true).KeyChar.ToString().ToLower())
    {
        case "y":
            wanttocontinue = true;
            break;
        case "n":
            Console.WriteLine("Спасибо за использование программы. Пока!");
            wanttocontinue = false;
            break;
        default:
            Console.WriteLine("Кто разрешал жать любую клавишу?! Вот и иди теперь отсюда");
            wanttocontinue = false;
            break;
    }
}