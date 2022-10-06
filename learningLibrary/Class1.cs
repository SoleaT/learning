namespace learningLibrary;

//функции нахождения максимума и минимума, заполнения массива строкой - неактуальны
public class myLearningClass
{
    public int InputNumbers() //ввод числа - на выходе получается int число, без вариантов, уруру
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

    public int CountDigits(int countNum) //считает сумму цифр в числе
    {
        int sum = 0;
        while (countNum > 0)
        {
            sum = sum + countNum % 10;
            countNum = countNum / 10;
        }
        return sum;
    }

    #region FillArrays

    // замены этой функции, но без проверки на вшивость:
    // int[] inputArray = Array.ConvertAll(Console.ReadLine().Split(" "), int.Parse);
    // int[] inputArray = Console.ReadLine()!.Split(separators).Select(int.Parse).ToArray();
    public int[] FillArrayFromString(string inputstring) //заполнение целочисленного массива из строки
    {
        char[] separators = { ' ', ',', ';' };
        string[] tempArray = inputstring.Split(separators);
        int[] newArray = new int[tempArray.Length];
        var r = new Random();
        for (int i = 0; i < tempArray.Length; i++)
        {
            try
            {
                newArray[i] = int.Parse(tempArray[i]);
            }
            catch (FormatException)
            {
                newArray[i] = r.Next(-10, 10);
                throw;
            }
        }
        return newArray;
    }

    public int[] FillRandomArray(int size, int firstNum, int secondNum) //заполнение целочисленного рандомного массива
    {
        int[] newArray = new int[size];
        for (int i = 0; i < size; i++)
            newArray[i] = new Random().Next(firstNum, secondNum);
        return newArray;
    }
    public double[] FillRandomArray(int size, double firstNum, double secondNum) //заполнение массива double рандомно
    {
        double[] newArray = new double[size];
        for (int i = 0; i < size; i++)
        {
            var rnd = new Random();
            newArray[i] = firstNum + rnd.NextDouble() * (secondNum - firstNum);
        }
        return newArray;
    }

    #endregion

    #region Max-Min-Average

    //замена этой функции - .Max()
    public int GetmaxNumberInArray(int[] newArray) //найти максимум в массиве. 
    {
        int maxNum = newArray[0];
        int size = newArray.Length;
        for (int i = 1; i < size; i++)
            if (newArray[i] > maxNum) maxNum = newArray[i];
        return maxNum;
    }

    //замена этой функции - .Min()
    public int GetminNumberInArray(int[] newArray) //найти минимум в массиве. 
    {
        int minNum = newArray[0];
        int size = newArray.Length;
        for (int i = 1; i < size; i++)
            if (newArray[i] < minNum) minNum = newArray[i];
        return minNum;
    }


    public double GetAverageFromArray(int[] newArray) //найти среднее арифм. массива
    {
        int sum = 0;
        int size = newArray.Length;
        for (int i = 0; i < size; i++)
            sum += newArray[i];
        return sum / size;
    }

    //замена этой функции - .Max()
    public double GetmaxNumberInArray(double[] newArray) //найти максимум в массиве double. 
    {
        double maxNum = newArray[0];
        int size = newArray.Length;
        for (int i = 1; i < size; i++)
            if (newArray[i] > maxNum) maxNum = newArray[i];
        return maxNum;
    }

    //замена этой функции - Array.Min()
    public double GetminNumberInArray(double[] newArray) //найти минимум в массиве double. 
    {
        double minNum = newArray[0];
        int size = newArray.Length;
        for (int i = 1; i < size; i++)
            if (newArray[i] < minNum) minNum = newArray[i];
        return minNum;
    }

    public double GetAverageFromArray(double[] newArray) //найти среднее арифм. массива double
    {
        double sum = 0;
        int size = newArray.Length;
        for (int i = 0; i < size; i++)
            sum += newArray[i];
        return sum / size;
    }
    #endregion

    public int CountEvenNumbers(int[] newArray) //найти кол-во чётных элементов в массиве
    {
        int sum = 0;
        int size = newArray.Length;
        for (int i = 0; i < size; i++)
        {
            if (newArray[i] % 2 == 0) sum++;
        }
        return sum;
    }
    public int CountSumOnEvenPositions(int[] array) //найти сумму элементов массива на чётных позициях
    {
        int sum = 0;
        int size = array.Length;
        for (int i = 0; i < size; i++)
            if (i % 2 != 0) sum += array[i];
        return sum;
    }
    public (int[] evenArray, int[] oddArray) MakeEvenoddArrays(int[] array) //делим массив на 2 массива: четных и нечетных чисел
    {
        int size = array.Length;
        List<int> evenArray = new List<int>();
        List<int> oddArray = new List<int>();
        for (int i = 0; i < size; i++)
        {
            if (array[i] % 2 == 0)
                evenArray.Add(array[i]);
            else
                oddArray.Add(array[i]);
        }
        return (evenArray.ToArray(), oddArray.ToArray());
    }

    public int[] MoveArrayToSide(int[] inputArray, char parameter) //сдвигает массив на 1 символ
    {
        int size = inputArray.Length;
        int[] newArray = new int[size];
        if (parameter == 'l')
        {
            Array.Copy(inputArray, 1, newArray, 0, size - 1);
            newArray[size - 1] = inputArray[0];
        }
        else if (parameter == 'r')
        {
            Array.Copy(inputArray, 0, newArray, 1, size - 1);
            newArray[0] = inputArray[size - 1];
        }
        return newArray;
    }

}

