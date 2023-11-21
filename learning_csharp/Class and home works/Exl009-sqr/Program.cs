//Написать программу, которая на вход принимает 2 числа и проверяет, является ли первое квадратом второго
Console.Write("Введите первое число: ");
int number1 = int.Parse(Console.ReadLine());
Console.Write("Введите второе число: ");
int number2 = int.Parse(Console.ReadLine());
if (number2 == Math.Pow(number1, 2))
{
    Console.WriteLine($"Да, первое число {number1} является квадратом второго {number2}");
}
else
{
    Console.WriteLine($"Нет, первое число {number1} не является квадратом второго {number2}");
}