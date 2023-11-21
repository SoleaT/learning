//программа, которая выводит третью цифру заданного числа или сообщает, что третьей цифры нет.

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
    }
    return number;
}
void doingMain() // ну поехали, на этой задаче, походу, споткнулись буквально все.
{
    int mynumber = Math.Abs(inputnumbers());
    while (mynumber / 1000 > 0)
        mynumber = mynumber / 10;
    if (mynumber / 100 <= 0)
        Console.WriteLine("Третьей цифры нет");
    else
        Console.WriteLine("Третья цифра - " + mynumber % 10);

/*  Вариант со строкой. Неспортивно, говорят. 
    int numlen = mynumber.ToString().Length;
    if (numlen > 3)
    {
        while (numlen > 3)
        {
            mynumber = mynumber / 10;
            numlen--;
        }
        Console.WriteLine("Третья цифра - " + mynumber % 10);
    }
    else if (numlen < 3)
        Console.WriteLine("Третьей цифры нет");
    else
        Console.WriteLine("Третья цифра - " + mynumber % 10);*/
}


bool wanttocontinue = true;
while (wanttocontinue)
{
    doingMain();
    Console.Write("Хотите ввести число ещё раз? (y/n)}");
    Console.WriteLine();

    switch (Console.ReadKey(true).Key.ToString().ToLower()) //вот эта монструозная конструкция вообще законна?
    {
        case "y":                                           //этот ваш свич не дает объединить рус и англ. 
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
