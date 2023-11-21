int numberA = 0;
int numberB = 0;
Console.WriteLine("Программа складывания двух чисел.");
bool isConverted = false;
while (isConverted != true)
{
    Console.Write("Введите первое число (целое): ");
    string input1 = Console.ReadLine();
    try
    {

        numberA = Convert.ToInt32(input1);
        isConverted = true;
    }
    catch (FormatException)
    {
        isConverted = false;
        Console.WriteLine("Неправильно задано число");
    }
}
//Console.WriteLine(numberA);
isConverted = false;
while (isConverted != true)
{
    Console.Write("Введите второе число (целое): ");
    string input2 = Console.ReadLine();
    try
    {

        numberB = Convert.ToInt32(input2);
        isConverted = true;
    }
    catch (FormatException)
    {
        isConverted = false;
        Console.WriteLine("Неправильно задано число");
    }
}
//Console.WriteLine(numberB);
int result = numberA + numberB;
Console.WriteLine("Сумма двух чисел: " + result);

