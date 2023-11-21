Console.WriteLine("Программа умножения двух случайных чисел");
double numberA = new Random().Next(1, 30), numberB = new Random().Next(1, 20);
Console.WriteLine("Число 1: " + numberA);
Console.WriteLine("Число 2: " + numberB);
double result = numberA * numberB;
Console.WriteLine("Результат умножения: " + result);
