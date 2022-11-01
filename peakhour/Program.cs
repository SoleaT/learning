using System.Linq;

Console.Clear();
System.Console.WriteLine(@"Суть задачи:
Есть магазин, в магазине охранник. Охранник ведёт запись всех входящих в магазин и уходящих из него.
Зайти и выйти можно в целый час. 
Выяснить, в какой промежуток времени (час) было больше всего посетителей.
Данные вводятся парами: приход уход. Максимум 100 покупателей.");

// (int h1, int h2)[] readData = new (int, int)[2];
System.Console.WriteLine("Скок надо строчек?");
int n=int.Parse(Console.ReadLine());
int i = 0;
(int h1,int h2)[] readData=new (int,int)[n];

while (true)
{
    readData = Console.ReadLine()
                  .Split(" ")
                  .Select(item => item.Split(" "))
                  .Select(a => (h1: int.Parse(a[0]), h2: int.Parse(a[1])))
                  .ToArray();
    // // System.Console.WriteLine(Console.ReadKey().Key);
    // if (readData.GetLength(0)>n) break;
    // System.Console.WriteLine(i);
    // if (readData[i].h1 == -1 || readData[i].h2 == -1) break;
    
    System.Console.WriteLine(readData);
    i++;
    System.Console.WriteLine(i);
    if (i >= n) break;
}

// System.Console.WriteLine(readData.GetLength(0));
// for (int j = 0; j < n; j++)
// {
//     System.Console.WriteLine(readData[j].h1+" "+readData[j].h2);
// }