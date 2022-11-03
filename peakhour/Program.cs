using System.Linq;

Console.Clear();
System.Console.WriteLine(@"Суть задачи:
Есть магазин, в магазине охранник. Охранник ведёт запись всех входящих в магазин и уходящих из него.
Зайти и выйти можно в целый час. 
Выяснить, в какой промежуток времени (час) было больше всего посетителей.
Данные вводятся парами: приход уход. Максимум 100 покупателей.");

System.Console.WriteLine("Введите часы посещения, 1 посетитель в строке, часы через пробел: ");
List<(int h1, int h2)> readData = new List<(int, int)>();
while (true)
{
    try
    {
        readData.Add(ParseOneString(Console.ReadLine()));
    }
    catch (System.Exception)
    {
        System.Console.WriteLine("Ввод закончен");
        break;
    }
}
System.Console.WriteLine("Посетителей: " + readData.Count);

int[] workingHours = new int[24];

for (int i = 0; i < readData.Count; i++)
    for (int j = readData[i].h1; j <= readData[i].h2; j++)
        workingHours[j]++;


int maxNumber = workingHours[0];
for (int i = 0; i < workingHours.Length; i++)
{
    if (workingHours[i] > maxNumber)
        maxNumber = workingHours[i];
}

string resultHours = "";
for (int i = 0; i < workingHours.Length - 1; i++)
{
    if (workingHours[i] == maxNumber && workingHours[i + 1] == maxNumber)
        resultHours += $" c {i} до {i + 1},";
}

System.Console.WriteLine("Интервалы наибольшего присутствия: {0}\b часов", resultHours);

(int, int) ParseOneString(string s)
{
    int[] temp = new int[2];
    try
    {
        temp = Array.ConvertAll(s.Split(" "), int.Parse);
    }
    catch (System.Exception)
    {
        throw new System.Exception("Ввод закончен");
    }
    if (temp[0]>temp[1])
        (temp[0],temp[1])=(temp[1],temp[0]);
    for (int i = 0; i < 2; i++)
    {
        if (temp[i] > 23)
            temp[i] = 0;
        if (temp[i] < 0)
            temp[i] = 24 - temp[i];
    }

    return (temp[0], temp[1]);
}