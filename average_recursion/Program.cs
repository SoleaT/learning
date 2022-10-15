Console.Clear();
System.Console.WriteLine(@"Суть задачи:
Написать программу, которая принимает от пользователя положительные числаи считает среднее значение этих чисел.
Ввод чисел осуществляется до тех пор, пока пользовател не введёт -1.
Ввод чисел и расчёт должен происходит в рекурсии");
SumAverage(0, 0);

void SumAverage(int n, double sum)
{
    System.Console.Write("Введите цифру: ");
    int input = int.Parse(Console.ReadLine() ?? "-1");
    if (input == -1)
    {
        System.Console.WriteLine($"Среднее арифметическое всех введённых цифр: {Math.Round(sum / n, 2)}");
        return;
    }
    SumAverage(++n, sum + input);
}
