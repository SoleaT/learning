// Написать программу, которая из сформированного массива строк, содержащих символы и числа, создает
// массив из строк, содержащих только символы, и чтоб не читерить
//не знаю, что включено в читерить, вроде постаралась без этого. так то программу можно сильно укоротить

Console.Clear();

System.Console.Write("Введите размерность массива: ");
int count = int.Parse(Console.ReadLine() ?? "10");
string[] firstarray = CreateRandomArray(count);
PrintArray(firstarray);
System.Console.WriteLine();
int j = 0;
foreach (string elem in firstarray)
{
    if (!CheckIsDigit(elem))
        j++;
}
string[] secondArray = new string[j];
j = 0;
for (int i = 0; i < count; i++)
{
    if (!CheckIsDigit(firstarray[i]))
    {
        secondArray[j] = firstarray[i];
        j++;
    }
}
PrintArray(secondArray);


string[] CreateRandomArray(int n)
{
    string[] tempArray = new string[n];
    string symbolString = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    var r = new Random();
    int k = symbolString.Length;
    for (int i = 0; i < n; i++)
    {
        if (r.Next(0, 2) == 1)
            tempArray[i] = symbolString[r.Next(0, k)].ToString();
        else
            tempArray[i] = r.Next(0, 10).ToString();
    }
    return tempArray;
}

void PrintArray(string[] tempArray)
{
    int n = tempArray.Length;
    System.Console.Write("Полученный массив: [");
    for (int i = 0; i < n; i++)
    {
        System.Console.Write("{0,2}", tempArray[i]);
    }
    System.Console.WriteLine(" ]");
}


bool CheckIsDigit(string s)
{
    for (int i = 0; i < 9; i++)
    {
        if (s.ToString() == i.ToString())
            return true;
    }
    return false;
}