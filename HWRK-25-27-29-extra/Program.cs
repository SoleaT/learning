// using learningLibrary;

myLearningClass CurrentHWRK = new myLearningClass();

int i = 0;
bool wanttocontinue = true;
while (wanttocontinue)
{
    //какую задачу хотим решить
    Console.Clear();
    Console.WriteLine(@"Есть 5 задач на выбор.
                    Задача 1: Напишите цикл, который принимает на вход два числа (A и B) и возводит число A в натуральную степень B.
                    Задача 2: Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе.
                    Задача 3: Напишите программу, которая задаёт массив из N элементов и выводит их на экран.
                    Задача 4: Напишите программу, которая задаёт массив из 10 элементов, которые необходимо заполнить случайными значениями в 
                    диапазоне от -10 до 10 и найти максимальное значение среди них.
                    Задача 5: Напишите программу, которая задаёт 2 одномерных массива из N элементов которые заполняются случайными значениями 
                    в диапазоне от 1 до 10 и находит среднее арифметическое элементов этих 2 массивов, далее от большего из получившихся средних 
                    арифметических отнимаем меньшее и округлённый до целого числа результат переводим в двоичную систему счисления.");

    System.Console.WriteLine("Выберите номер задачи (1 2 3 4 5): ");
    int numofwork = CurrentHWRK.InputNumbers();

    switch (numofwork) //разбор по задачам
    {
        case 1:
            System.Console.Write("Введите число А: ");
            int numA = CurrentHWRK.InputNumbers();
            System.Console.Write("Введите число B: ");
            int numB = CurrentHWRK.InputNumbers();
            int deg = numA;
            for (i = 1; i < numB; i++) //не вижу смысла писать для этого отдельную функцию, ведь всегда есть math.pow
            {
                deg = deg * numA;
            }
            System.Console.WriteLine("Число {0} в степени {1} равно {2}", numA, numB, deg);
            break;
        case 2:
            System.Console.Write("Введите число:");
            int inpnumber = CurrentHWRK.InputNumbers();
            System.Console.WriteLine("Сумма цифр в числе " + inpnumber + " равна " + CurrentHWRK.countDigits(Math.Abs(inpnumber)));
            break;
        case 3:
            System.Console.WriteLine("Введите массив строкой через пробел: ");        //работайте, негры! такого заполнения у нас ещё не было
            System.Console.WriteLine("Массив элементов: " + string.Join("|", CurrentHWRK.fillArrayFromString(System.Console.ReadLine() ?? "1 2 3"))); //кому-то лень сделать проверку на дурака
            break;
        case 4:
            int[] randomarr = CurrentHWRK.fillRandomArray(10, -10, 10);
            System.Console.WriteLine($"Получился массив: {string.Join("|", randomarr)}\nМаксимальное число в нём: {CurrentHWRK.getMaxNumberInArray(randomarr)}\n");
            break;
        case 5:
            System.Console.Write("Введите размерность первого массива N1: ");
            int n1 = CurrentHWRK.InputNumbers();
            int[] array1 = CurrentHWRK.fillRandomArray(n1, 1, 10);
            System.Console.Write("Введите размерность второго массива N2: ");
            int n2 = CurrentHWRK.InputNumbers();
            int[] array2 = CurrentHWRK.fillRandomArray(n2, 1, 10);
            double sum1 = CurrentHWRK.getAverageFromArray(array1);
            double sum2 = CurrentHWRK.getAverageFromArray(array2);
            int sum = sum1 > sum2 ? Convert.ToInt32(Math.Round(sum1 - sum2)) : Convert.ToInt32(Math.Round(sum2 - sum1));

            // System.Console.WriteLine(Convert.ToString(sum,2)); //ну ведь не о таком способе была речь, да? :)

            //поэтому будем чесать левое ухо правой пяткой
            System.Console.Write($"Полученное число {sum} в двоичном значении: ");
            List<int> reversenum = new List<int>();
            while (sum > 0)
            {
                reversenum.Add(sum % 2);
                sum = sum / 2;
            }
            for (int j = reversenum.Count; j > 0; j--)
                System.Console.Write(reversenum[j - 1]);
            System.Console.WriteLine("\n");
            break;
        default:
            Console.WriteLine("Такую задачу ещё не решали. Выбирайте цифру с умом.");
            break;
    }
    Console.WriteLine("Хотите решить ещё задачу? (y/n)}");
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

class myLearningClass
{
    public int InputNumbers()
    {
        int number = 0;
        bool isConverted = false;
        while (isConverted != true)
        {
            string input1 = Console.ReadLine() ?? "-r";
            try
            {
                number = Convert.ToInt32(input1);
                isConverted = true;
            }
            catch (FormatException)
            {
                isConverted = false;
                Console.WriteLine("Неправильно задано число. Введите заново: ");
            }
        }
        return number;
    }

    public int countDigits(int countnum)
    {
        int sum = 0;
        while (countnum > 0)
        {
            sum = sum + countnum % 10;
            countnum = countnum / 10;
        }
        return sum;
    }

    public int[] fillArrayFromString(string inputstring)
    {
        string[] temparray = inputstring.Split(" ");
        int[] newarray = new int[temparray.Length];
        for (int i = 0; i < temparray.Length; i++)
        {
            try
            {
                newarray[i] = int.Parse(temparray[i]);
            }
            catch (FormatException)
            {
                newarray[i] = -1;
                throw;
            }
        }
        return newarray;
    }

    public int[] fillRandomArray(int arraylength, int firstnum, int secondnum)
    {
        int[] newarray = new int[arraylength];
        for (int i = 0; i < arraylength; i++)
            newarray[i] = new Random().Next(firstnum, secondnum);
        return newarray;
    }
    public double[] fillRandomArray(int arraylength, double firstnum, double secondnum)
    {
        double[] newarray = new double[arraylength];
        for (int i = 0; i < arraylength; i++)
        {
            var rnd = new Random();
            newarray[i] = firstnum + rnd.NextDouble() * (secondnum - firstnum);
        }
        return newarray;
    }

    public int getMaxNumberInArray(int[] newarray)
    {
        int maxnum = newarray[0];
        for (int i = 1; i < newarray.Length; i++)
            if (newarray[i] > maxnum) maxnum = newarray[i];
        return maxnum;
    }

    public double getAverageFromArray(int[] newarray)
    {
        int sum = 0;
        for (int i = 0; i < newarray.Length; i++)
            sum += newarray[i];
        return sum / newarray.Length;
    }
}

