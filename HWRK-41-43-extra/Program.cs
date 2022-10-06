using learningLibrary;

myLearningClass currentWork = new myLearningClass();

bool wantToContinue = true;
while (wantToContinue)
{
    //какую задачу хотим решить
    Console.Clear();
    Console.WriteLine(@"Есть 4 задачи на выбор.
                        Задача 1: Пользователь вводит с клавиатуры M чисел. Посчитайте, сколько чисел больше 0 ввёл пользователь.
                        Задача 2: Напишите программу, которая найдёт точку пересечения двух прямых, заданных уравнениями 
                        y = k1 * x + b1, y = k2 * x + b2; значения b1, k1, b2 и k2 задаются пользователем.
                        Задача 3: Массив из n случайных элементов необходимо сдвинуть влево или вправо на 1 позицию.
                        Задача 4: В массиве из n случайных элементов необходимо определить существует ли пара соседних элементов с 
                        одинаковыми значениями, при наличии такого элемента заменить его на уникальное значение.");

    System.Console.WriteLine("Выберите номер задачи (1 2 3 4): ");
    int numOfWork = currentWork.InputNumbers();
    int size = new Random().Next(10, 30);
    char[] separators = { ' ', ',', ';' };

    switch (numOfWork) //разбор по задачам
    {
        case 1:
            System.Console.WriteLine("Введите числа в строку через пробел: ");
            Console.Write("Введите элементы(через пробел): ");

            //тут какой из вариантов эффективней?
            // int[] inputarray = Array.ConvertAll(Console.ReadLine().Split(separators), int.Parse); 
            int[] inputarray = Console.ReadLine()!.Split(separators).Select(int.Parse).ToArray();

            //классик
            // size=array.Length;
            // int count=0;
            // for (int i=0;i<size;i++)                        
            //     if (array[i]>0) count++;
            // System.Console.WriteLine($"Вы ввели {count} чисел больше 0");

            //неклассик. есть прогресс: я знаю, что b=>b>0 это лямбда-выражение, но что оно и как работает - всё ещё не знаю :'( 
            int[] temparray = Array.FindAll(inputarray, b => b > 0);
            System.Console.WriteLine($"Вы ввели {temparray.Length} чисел больше 0, от таких: {string.Join(" ", temparray)}");
            break;
        case 2:
            System.Console.WriteLine("Введите значения k1 b1 k2 b2 через пробел: ");
            double[] coords = Console.ReadLine()!.Split(separators).Select(double.Parse).ToArray();
            if (coords[0] == coords[2])
            {
                if (coords[0] == coords[1])
                {
                    System.Console.WriteLine("Прямые совпадают");
                    break;
                }
                else
                {
                    System.Console.WriteLine("Прямые параллельны");
                    break;
                }
            }
            double x = (coords[3] - coords[1]) / (coords[0] - coords[2]);
            double y = coords[2] * x + coords[3];
            Console.WriteLine($"Точка пересечения имеет координаты {Math.Round(x, 2)},{Math.Round(y, 2)}");
            break;
        case 3:
            System.Console.WriteLine("Задайте размерность массива: ");
            size = currentWork.InputNumbers();
            int[] newArray = currentWork.FillRandomArray(size, -10, 10);
            System.Console.WriteLine("Куда сдвинуть? Нажмите стрелку влево или вправо");
            var key = Console.ReadKey(true).Key;
            switch (key)
            {
                case ConsoleKey.LeftArrow:
                    System.Console.WriteLine($"Значит, влево. [{string.Join(",", newArray)}]->[{string.Join(",", currentWork.MoveArrayToSide(newArray, 'l'))}]");
                    break;
                case ConsoleKey.RightArrow:
                    System.Console.WriteLine($"Значит, вправо. [{string.Join(",", newArray)}]->[{string.Join(",", currentWork.MoveArrayToSide(newArray, 'r'))}]");
                    break;
                default:
                    System.Console.WriteLine("Мы таких стрелок не знаем");
                    break;
            }
            break;
        case 4:
            size = 8;
            int[] newArray2 = currentWork.FillRandomArray(size, 5, 10); //да, опять заполняю массив, но ведь в первых двух задачах его не было
            int yPosOld=Console.CursorTop,
                yPos = yPosOld + 2;
            System.Console.WriteLine($"У нас есть массив [{string.Join(" ", newArray2)}]");
            bool checkNumber = false;
            bool weFoundIt = false;
            var r = new Random();
            for (int i = 0; i < size - 1; i++)   //если можно сделать это короче с помощью какие-нибудь существующих методов, я бы хотела знать, как
            {
                if (newArray2[i] == newArray2[i + 1])
                {
                    Console.ForegroundColor = ConsoleColor.Cyan;
                    System.Console.WriteLine($"Найдены соседние повторяющиеся цифры на местах {i} и {i+1}");
                    Console.SetCursorPosition(19 + i * 2, yPosOld);
                    Console.Write($"{newArray2[i]} {newArray2[i + 1]}");
                    Console.SetCursorPosition(0, yPos++);
                    weFoundIt = true;
                    while (!checkNumber)
                    {
                        int uniqnum = r.Next(0, 10);
                        if (!Array.Exists(newArray2, elem => elem == uniqnum))
                        {
                            newArray2[i+1] = uniqnum;
                            checkNumber = true;
                        }
                    }
                    checkNumber = false;
                }
            }
            Console.ResetColor();
            if (weFoundIt) System.Console.WriteLine($"После замены получился массив: [{string.Join(" ", newArray2)}]");
            else System.Console.WriteLine("Повторяющиеся цифры не найдены");
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
