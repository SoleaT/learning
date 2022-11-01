//потраим делегаты
//это сложный босс

using System.Linq;
Console.Clear();

System.Console.Write("размерность массива: ");
int n = int.Parse(Console.ReadLine()!);

//объявляем список объектов. в объекте 3 поля, см внизу
List<RandObject> newList = new List<RandObject>();

// переменная на все случаи жизни
var r = new Random();

// макс целое число
int maxNum = r.Next(10, 100); 

// алфавит для формирования строки
string symbolString = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

for (int i = 0; i < n; i++)
    FillRandomField();

PrintArray();

System.Console.WriteLine("По какому столбцу сортирнуть? 1 2 3");
int col = int.Parse(Console.ReadLine()!);

//запускаем сортировку по типам данным с вызовом нужной функции через функцию с делегатом
switch (col)
{
    case 1:
        ProcessSort(sortString);
        break;
    case 2:
        ProcessSort(sortInteger);
        break;
    case 3:
        ProcessSort(sortChar);
        break;
    default:
        System.Console.WriteLine("Такого нет, пока");
        break;
}

PrintArray();

// функция сортировки, через которую вызываем делегата
void ProcessSort(SortingCallback sort)
{
    for (int i = 0; i < newList.Count(); i++)
        for (int j = 0; j < i; j++)
            if (sort(newList[i], newList[j]) == -1)
            {
                (newList[i], newList[j]) = (newList[j], newList[i]);
            }
}

// отдельные функции сравнения объектов
int sortInteger(RandObject num1, RandObject num2)
{
    if (num1.intField > num2.intField) return 1;
    else if (num1.intField < num2.intField) return -1;
    else return 0;
}

int sortString(RandObject str1, RandObject str2)
{
    if (str1.strField.Length > str2.strField.Length) return 1;
    else if (str1.strField.Length < str2.strField.Length) return -1;
    else return 0;
}

int sortChar(RandObject ch1, RandObject ch2)
{
    if (ch1.charField > ch2.charField) return 1;
    else if (ch1.charField < ch2.charField) return -1;
    else return 0;
}

// заполняем одно поле
// почему одно - ну вдруг с клавы захочется ввести отсюда и до -1, меньше переписывать
void FillRandomField()
{
    int maxWordLength = r.Next(1, 10); //макс длина слова, для каждого слова может быть разная
    string randString = FormString(r.Next(1, maxWordLength));
    newList.Add(new RandObject(randString, r.Next(0, maxNum), symbolString[r.Next(0, symbolString.Length)]));
}

// формирование строки символов
string FormString(int size)
{
    if (size == 0) return symbolString[r.Next(0, symbolString.Length)].ToString();
    return symbolString[r.Next(0, symbolString.Length)] + FormString(size - 1);
}

void PrintArray()
{
    int n = newList.Count();
    System.Console.WriteLine("Полученный массив:");
    for (int i = 0; i < n; i++)
    {
        System.Console.WriteLine("({0,10}, {1,3}, {2,2})", newList[i].strField, newList[i].intField, newList[i].charField);
    }
}

// объект с 3 полями: строковое, целочисленное, символьное
struct RandObject
{
    public string strField;
    public int intField;
    public char charField;

    public RandObject(string str, int intg, char chr)
    {
        strField = str;
        intField = intg;
        charField = chr;
    }
}

// объявляем делегат для сравнения объектов
delegate int SortingCallback(RandObject a, RandObject b);

// победила (⌒‿⌒)