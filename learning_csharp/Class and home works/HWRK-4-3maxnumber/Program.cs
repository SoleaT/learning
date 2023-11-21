//Напишите программу, которая принимает на вход три числа и выдаёт максимальное из этих чисел.

int inputnumbers(string numorder)
{
    int number = 0;
    bool isConverted = false;
    while (isConverted != true)
    {
        Console.Write($"Введите {numorder} число (целое): ");
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

Console.WriteLine("Для работы программы необходимо задать 3 числа.");

int numberA = inputnumbers("первое");
int numberB = inputnumbers("второе");
int numberC = inputnumbers("третье");

int maxnumber = numberA;
if (numberB > maxnumber)
{
    maxnumber = numberB;
}
if (numberC > maxnumber)
{
    maxnumber = numberC;
}
Console.WriteLine("Максимальное число из трёх: " + maxnumber);