//задачи для домашки 3семинара, все в одном
Console.Clear();
int inputnumbers(string whattowrite) //дык это просто циферки вводить, целые. в аргументах - что подписать в запросе
{
    int number = 0;
    bool isConverted = false;
    while (isConverted != true)
    {
        Console.Write(whattowrite);
        string input1 = Console.ReadLine() ?? "-r";
        try
        {
            number = Convert.ToInt32(input1);
            isConverted = true;
        }
        catch (FormatException)
        {
            isConverted = false;
            Console.WriteLine("Неправильно задано число");
        }
    }
    return number;
}

//для задачи 19
//принимает на вход пятизначное число и проверяет, является ли оно палиндромом.

bool isPalindrome(int checknum)
{
    int secnum = 0;
    int temp = checknum;
    for (int i = 0; i < 5; i++)
    {
        secnum = secnum * 10 + temp % 10;
        temp = temp / 10;
    }

    if (secnum == checknum) return true;
    else return false;
}

// задача 21 принимает на вход координаты двух точек и находит расстояние между ними в 3D пространстве.
// формула d=sqrt((xb-xa)^2+(yb-ya)^2+(zb-za)^2);
// самая сложная функция века

double calc3Ddistance(int[,] coords)
{
    return Math.Sqrt(Math.Pow((coords[0, 1] - coords[0, 0]), 2) + Math.Pow(coords[1, 1] - coords[1, 0], 2) + Math.Pow(coords[2, 1] - coords[2, 0], 2));
}

//для задачи 23
//принимает на вход число (N) и выдаёт таблицу кубов чисел от 1 до N.
void writecubes(int number)
{
    Console.Write($"Кубы чисел от 1 до {number}: ");
    for (int i = 1; i <= number; i++)
    {
        Console.Write(Math.Pow(i, 3) + " | ");
    }
}

void maxnumber(int number) //выводим максимальную цифру для заданного числа
{
    int nummax = 0;
    int numrest = 0;
    while (number > 10)
    {
        numrest = number % 10;
        if (nummax < numrest) nummax = numrest;
        number = number / 10;
    }
    Console.WriteLine($"Максимальная цифра = {nummax}");
}

// для задачи 5 - названия городов, где больше всего вхождений введенного символа
void printcity(string[] arraycity, char findchar)    //есть у меня подозрение, что где-то в функции можно сократить, оно оправдано?
{
    int[] occurence = new int[arraycity.Length];
    int j = 0;
    if (findchar == '0')
    {
        findchar = 'а';
        Console.WriteLine("Была введена пустая строка, так что назначим букву а");
    }
    foreach (string city in arraycity)
    {
        int numofchar = 0;
        for (int i = 0; i < city.Length; i++)
        {
            if (city[i] == findchar) numofchar++;
        }
        occurence[j] = numofchar;
        j++;
    }
//  Console.WriteLine("ЧИсла вхождений " + string.Join(" ", occurence));
    int maxnumofchar = occurence.Max();     
    Console.Write($"Города, где больше всего букв {findchar}({maxnumofchar}): ");
    for (int k = 0; k < occurence.Length; k++)
        if (occurence[k] == maxnumofchar) Console.Write($"{arraycity[k]} ");
    Console.WriteLine();
}

//-________________________________________________________________________________________- это такая широкая улыбка

bool wanttocontinue = true;
while (wanttocontinue)
{
    //какую задачу хотим решить
    Console.WriteLine(@"Есть 5 задач на выбор.
                    Задача1: принимает на вход пятизначное число и проверяет, является ли оно палиндромом.
                    Задача2: принимает на вход координаты двух точек и находит расстояние между ними в 3D пространстве.
                    Задача3: принимает на вход число (N) и выдаёт таблицу кубов чисел от 1 до N.
                    Задача4: на вход принимает радиус круга и находит его площадь округленную до целого числа, 
                             необходимо вывести максимальную цифру в полученном округлённом значении площади круга.
                    Задача5: на вход принимает букву, необходимо создать массив из 5 названий городов, и вывести на экран те (тот), 
                             где чаще всего встречается введённая буква.");
    int numofwork = inputnumbers("Выберите номер задачи (1 2 3 4 5): ");

    switch (numofwork) //разбор по задачам
    {
        case 1:
            int number5 = inputnumbers("Введите пятизначное число: ");
            if (number5 > 9999 && number5 < 100000)  //есть подозрение, что это тоже какой-то костыль и можно сделать нормально
            {
                if (isPalindrome(number5))
                    Console.WriteLine($"Число {number5} является палиндромом.");
                else
                    Console.WriteLine($"Число {number5} не является палиндромом.");
            }
            else
                Console.WriteLine($"Число {number5} не пятизначное.");
            break;
        case 2:
            int[,] coords = new int[3, 2];     //я хз зачем так сложно. спорим - кроме меня, таких извращенцев не найдётся?
            int rows = coords.GetUpperBound(0) + 1; //скажем, массивы изучаю. матрицы. 
            int columns = coords.Length / rows; //=coords.GetUpperBound(1)+1;
            for (int i = 0; i < rows; i++)
            {
                for (int j = 0; j < columns; j++)
                {
                    if (i == 0) coords[i, j] = inputnumbers("Введите координату x" + (j + 1) + ": ");     //экономия такая себе
                    else if (i == 1) coords[i, j] = inputnumbers("Введите координату y" + (j + 1) + ": "); //matrix has you
                    else coords[i, j] = inputnumbers("Введите координату z" + (j + 1) + ": ");
                }
            }
            Console.WriteLine("Расстояние между двумя точками в 3D пространстве = " + Math.Round(calc3Ddistance(coords), 3));
            break;
        case 3:
            writecubes(inputnumbers("Введите число N: "));
            break;
        case 4:
            // int radius = inputnumbers("Введите радиус круга: ");
            maxnumber(Convert.ToInt32(Math.Round((Math.Pow(inputnumbers("Введите радиус круга: "), 2) * Math.PI))));
            break;
        case 5:
            string[] cities = new string[5] { "Санкт-Петербург", "Переславль-Залесский", "Феодосия", "Волгоград", "Джезказган" };
            Console.WriteLine("Дан массив городов: " + string.Join(", ", cities));
            Console.WriteLine("Какую букву найти? ");
            printcity(cities, Convert.ToChar(Console.ReadLine() ?? "0"));
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
