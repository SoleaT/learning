//программа, которая принимает на вход трёхзначное число и на выходе показывает вторую цифру этого числа.

Console.Clear();

int inputnumbers()
{
    int number = 0;
    bool isConverted = false;
    while (isConverted != true)
    {
        Console.Write($"Введите число (целое): ");
        string input1 = Console.ReadLine();
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
        if (input1.Length != 3)
        {
            isConverted = false;
            Console.WriteLine("Число не трёхзначное");
        }
    }
    return number;
}
void doingMain() // эта функция, собственно, и выполняет задание. самая сложная тут!
{
    int mynumber = inputnumbers();
    int seconddigit = mynumber % 100 / 10;
    Console.WriteLine($"Было введено число {mynumber}, его вторая цифра - {seconddigit}");
}

bool wanttocontinue = true;
while (wanttocontinue)
{
    doingMain();
    Console.Write("Хотите ввести число ещё раз? (y/n)}");
    Console.WriteLine();

    switch (Console.ReadKey(true).Key.ToString().ToLower()) //вот эта монструозная конструкция вообще законна?
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
