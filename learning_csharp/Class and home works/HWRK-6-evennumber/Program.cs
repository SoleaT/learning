//Напишите программу, которая на вход принимает число и выдаёт, является ли число чётным (делится ли оно на два без остатка).

double inputnumbers()
{
    double number = 0;
    bool isConverted = false;
    while (isConverted != true)
    {
        Console.Write("Введите число: ");
        string input1 = Console.ReadLine();
        try
        {
            number = Convert.ToDouble(input1);
            isConverted = true;
        }
        catch (FormatException)
        {
            isConverted = false;
            Console.WriteLine("Неправильно задано число (для веществ. чисел используйте ,)");
        }
    }
    return number;
}

Console.WriteLine("Программа, которая на вход принимает число и выдаёт, является ли число чётным");

double numberA = inputnumbers();

if (numberA % 2 == 0)
{
    Console.WriteLine($"Число {numberA} является чётным");
}
else
{
    Console.WriteLine($"Число {numberA} является нечётным");
}