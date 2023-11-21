//Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.

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

Console.WriteLine("Программа принимает число и выводит все чётные числа от 1 до введённого числа.");
Console.WriteLine("Для работы программы необходимо задать число.");

int numberA = inputnumbers();

int count = 1;

Console.Write($"Чётные числа от 1 до {numberA}: ");
while (count <= numberA)
{
    if (count % 2 == 0)
    {
        Console.Write(count + " ");
    }
    count++;
}