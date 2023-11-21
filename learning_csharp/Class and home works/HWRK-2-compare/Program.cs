//Напишите программу, которая на вход принимает два числа и выдаёт, какое число большее, а какое меньшее.

int inputnumbers()
{
    int number = 0;
    bool isConverted = false;
    while (isConverted != true)
    {
        Console.Write("Введите число (целое): ");
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

Console.WriteLine("Нужно ввести 2 числа для сравнения.");
int numberA = inputnumbers();
int numberB = inputnumbers();
if (numberA > numberB)
{
    Console.WriteLine($"Первое число {numberA} больше, чем второе число {numberB}");
}
else if (numberA < numberB)
{
    Console.WriteLine($"Второе число {numberB} больше, чем первое число {numberA}");
}
else
{
    Console.WriteLine($"Числа {numberA} и {numberB} равны");
}