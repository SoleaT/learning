Console.Clear();



// Напишите программу, которая будет преобразовывать десятичное число в двоичное
// System.Console.WriteLine("Введите число в десятичном формате: ");
// int number = int.Parse(System.Console.ReadLine());

// // System.Console.WriteLine(Convert.ToString(number,2);

// System.Console.Write($"Полученное число {number} в двоичном значении: ");
// List<int> reversenum = new List<int>();
// while (number > 0)                
// {
//     reversenum.Add(number % 2);
//     number = number / 2;
// }
// for (int j = reversenum.Count; j > 0; j--)
//     System.Console.Write(reversenum[j - 1]);

// Не используя рекурсию, выведите первые N чисел Фибоначчи.


// System.Console.WriteLine("Введите число: ");
// int number = int.Parse(System.Console.ReadLine());
// int i = 1;
// List<int> array = new List<int>() { 0, 1 };
// while (i < number - 1)
// {
//     array.Add(array[i] + array[i - 1]);
//     i++;
// }
// System.Console.WriteLine("Числа Фибоначчи: " + string.Join("|", array));

// Напишите программу, которая будет создавать копию заданного массива с помощью поэлементного копирования

// int[] FillArray()
// {
//     int n=new Random().Next(5,10);
//     int[] newarray=new int[n];
//     for (int i = 0; i < n; i++)
//     {
//         newarray[i]=new Random().Next(1,20);
//     }
//     return newarray;
// }

// int[] newarray=FillArray();
// System.Console.WriteLine("Первый массив: "+string.Join("|",newarray));
// int[] secondarray=new int[newarray.Length];
// for (int j=0;j<newarray.Length;j++)
// {
//     secondarray[j]=newarray[j];
// }
// System.Console.WriteLine("Копия массива: "+string.Join("|",secondarray));

// // Напишите программу, которая принимает на вход три числа и проверяет, может ли существовать треугольник с сторонами такой длины
// // Теорема о неравенстве треугольника: каждая сторона треугольника меньше суммы двух других сторон.
// Console.Clear();

// int InputNumbers()
// {
//     System.Console.Write("Введите число: ");
//     int a = int.Parse(Console.ReadLine());
//     return a;
// }

// System.Console.WriteLine("Нужно задать 3 числа для сторон треугольника");
// int a = InputNumbers();
// int b = InputNumbers();
// int c = InputNumbers();

// if (a<b+c && b<a+c && c<a+b)
//     System.Console.WriteLine("Такой треугольник может существовать");
// else
//     System.Console.WriteLine("Такой треугольник не может существовать");


// Рассчитать значение y при заданном x по формуле

// Console.Clear();

// double dofunction(double x)
// {
//     if (x > 0)
//         return Math.Round(Math.Pow(Math.Sin(x), 2), 2);
//     else
//         return Math.Round(1 - 2 * Math.Sin(Math.Pow(x, 2)), 2);
// }

// Console.Write("Введите х: ");
// Console.WriteLine("Значение у = " + dofunction(Convert.ToDouble(Console.ReadLine())));





/* Console.WriteLine("Введите номер плоскости: ");
int numofsqr=int.Parse(Console.ReadLine() ?? "0");

switch(numofsqr)
{
    case 1:
        Console.WriteLine("Доступные значения: х от 0 до +бесконечности, y от 0 до +бесконечности");
        break;
    case 2:
        Console.WriteLine("Доступные значения: х от -бесконечности до 0, y от 0 до +бесконечности");
        break;
    case 3:
        Console.WriteLine("Доступные значения: х от -бесконечности до 0, y от -бесконечности до 0");
        break;
    case 4:
        Console.WriteLine("Доступные значения: х от 0 до +бесконечности, y от -бесконечности до 0");
        break;
    default:
        Console.WriteLine("Неверная цифра");
}
*/




/*int rndnum = new Random().Next(100, 1000);
Console.WriteLine("Сгенерировано число " + rndnum);
int newnum = (rndnum / 100) * 10 + rndnum % 10;
Console.WriteLine($"Получено число {newnum}");*/

//принимает 2 числа и выводит, кратно ли второе число первому. если не кратно, то выводит остаток
/*int number1 = int.Parse(Console.ReadLine()), number2 = int.Parse(Console.ReadLine());
int ostatok = number1 % number2;
if (ostatok != 0)
    Console.WriteLine("Число 2 не кратно числу 1, остаток от деления " + ostatok);
else
    Console.WriteLine("Число 2 кратно числу 1");
*/



