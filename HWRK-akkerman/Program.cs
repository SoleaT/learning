// Напишите программу вычисления функции Аккермана с помощью рекурсии. Даны два неотрицательных числа m и n.

System.Console.WriteLine("Задача: Напишите программу вычисления функции Аккермана с помощью рекурсии");
System.Console.WriteLine("Введите числа m и n через пробел. Очень нежелательно m задавать больше 3, чтоб мы тут не улетели в космос с расчетами");
char[] separators = { ' ', ',', ';' };
int[] mn = Array.ConvertAll(Console.ReadLine()!.Split(separators), int.Parse);
System.Console.WriteLine(CalcAkkermanF(mn[0],mn[1]));

int CalcAkkermanF(int m, int n)
{
    if (m == 0)
        return n + 1;
    else if (m > 0 & n == 0)
        return CalcAkkermanF(m - 1, 1);
    else if (m > 0 & n > 0)
        return CalcAkkermanF(m - 1, CalcAkkermanF(m, n - 1));
    else return -1;
}