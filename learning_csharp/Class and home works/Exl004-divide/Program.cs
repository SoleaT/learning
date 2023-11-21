double numberA = 0, numberB = 0;
Console.WriteLine("Программа деления двух чисел.");
bool isConverted = false;
while (isConverted != true)
{
    Console.Write("Введите первое число: ");
    string input1 = Console.ReadLine();
    try
    {

        numberA = Convert.ToDouble(input1);
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
    Console.Write("Введите второе число: ");
    string input2 = Console.ReadLine();
    try
    {

        numberB = Convert.ToDouble(input2);
        isConverted = true;
    }
    catch (FormatException)
    {
        isConverted = false;
        Console.WriteLine("Неправильно задано число");
    }
}
//Console.WriteLine(numberB);
double result = numberA / numberB;
result=Math.Round(result,2);
Console.WriteLine("Частное двух чисел: " + result);

