//программа, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

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
            if (number > 7 || number < 1) //а можно в одну конструкцию объединить?
            {
                Console.WriteLine("Нет дней недели с такими цифрами");
                isConverted = false;
            }
            else
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
void doingMain() 
{
    int mynumber = inputnumbers();
    if (mynumber==6 || mynumber==7)
        Console.WriteLine("Этот день недели - выходной");
    else
        Console.WriteLine("Этот день недели - рабочий");
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
