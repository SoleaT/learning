Console.Clear();

const int wordLength=3;

System.Console.WriteLine("Желаете ввести массив с клавиатуры или заполнить случайно? k/r");
//массивы могут быть разные, так что придётся разные переменные делать. 
//а нечего было запрещать коллекции!

switch (Console.ReadKey().KeyChar.ToString().ToLower())
{
    case "r":
        System.Console.Write("\nЗадайте желаемую размерность массива: ");
        int arrayLength = InputNumbers();
        string[] stringArrayR = FillArrayRandomized(arrayLength,9);
        PrintArray(stringArrayR);
        string[] newStringArrayR = MakeShortArray(stringArrayR,wordLength);
        System.Console.WriteLine("->");
        PrintArray(newStringArrayR);
        break;
    case "k":
        System.Console.WriteLine("\nВведите слова через пробел: ");
        string[] stringArrayS = FillArrayFromString(Console.ReadLine() ?? "q w");
        PrintArray(stringArrayS);
        string[] newStringArrayS = MakeShortArray(stringArrayS,wordLength);
        System.Console.WriteLine("->");
        PrintArray(newStringArrayS);
        break;
    default:
        System.Console.WriteLine("\nНе понял эту букву :(");
        break;
}



#region Methods

string[] FillArrayFromString(string inputstring)
{
    char[] separators = { ' ', ',', ';' };
    string[] tempArray = inputstring.Split(separators);
    return tempArray;
}

string[] FillArrayRandomized(int arrayLength,int maxLength)
{
    string symbolString = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    int symbolStringLength = symbolString.Length;
    string[] tempArray = new string[arrayLength];
    var r = new Random();
    for (int i = 0; i < arrayLength; i++)
    {
        int n = r.Next(1, maxLength);
        for (int j = 0; j < n; j++)
        {
            tempArray[i] += symbolString[r.Next(0, symbolStringLength)];
        }
    }
    return tempArray;
}

void PrintArray(string[] tempArray)
{
    int arrayLength = tempArray.Length;
    if (arrayLength == 0)
    {
        System.Console.WriteLine("Массив пуст");
        return;
    }
    System.Console.Write("Массив: [");
    for (int i = 0; i < arrayLength; i++)
    {
        System.Console.Write(tempArray[i] + " ");
    }
    System.Console.WriteLine("\b]");
}

int InputNumbers()
{
    int number = 0;
    bool isConverted = false;
    while (isConverted != true)
    {
        string input1 = Console.ReadLine() ?? "-r";
        try
        {
            number = Convert.ToInt32(input1);
            isConverted = true;
        }
        catch (FormatException)
        {
            isConverted = false;
            Console.WriteLine("Неправильно задано число");
        }
    }
    return number;
}

string[] MakeShortArray(string[] tempArray, int maxLength)
{
    int arrayLength = tempArray.Length;
    int n = 0;
    for (int i = 0; i < arrayLength; i++)
    {
        if (tempArray[i].Length <= maxLength)
            n++;
    }
    string[] newArray = new string[n];
    n = 0;
    for (int i = 0; i < arrayLength; i++)
    {
        if (tempArray[i].Length <= maxLength)
        {
            newArray[n] = tempArray[i];
            n++;
        }
    }
    return newArray;
}

#endregion