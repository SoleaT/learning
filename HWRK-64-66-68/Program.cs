Console.Clear();

System.Console.WriteLine(@"64. Задайте значения N и M. Напишите программу, которая выведет все чётные натуральные числа в промежутке от M до N с помощью рекурсии.
66. Задайте значения M и N. Напишите программу, которая найдёт сумму натуральных элементов в промежутке от M до N с помощью рекурсии.
68. Задайте значения M и N. Напишите программу, которая найдёт наибольший общий делитель (НОД) этих чисел с помощью рекурсии.");

System.Console.WriteLine("Так что задайте числа m и n (через , или пробел):");
char[] separators = { ' ', ',', ';' };
int[] mn = Array.ConvertAll(Console.ReadLine()!.Split(separators), int.Parse);

if (mn[0] > mn[1])
    (mn[0], mn[1]) = (mn[1], mn[0]);
System.Console.Write("64: ");
Task64(mn[0], mn[1]);
System.Console.WriteLine("\n66: Сумма равна " + Task66(mn[0], mn[1]));
Task68(mn[0], mn[1]);

void Task64(int m, int n)
{
    if (m > n) return;
    if (m % 2 == 0 & m > 0) System.Console.Write(m + " ");
    Task64(m + 1, n);
}

int Task66(int sum, int n)
{
    if (sum >= n) return sum;
    if (sum > 0)
        sum += Task66(sum + 1, n);
    return sum;
}

void Task68(int m, int n)
{
    if (m == n)
    {
        System.Console.WriteLine("68: Наибольший общий делитель равен " + m);
        return;
    }
    if (m > n)
        (m, n) = (n, m);
    Task68(m, n - m);
}