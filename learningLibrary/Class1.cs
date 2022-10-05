namespace learningLibrary;
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

    public int CountDigits(int countnum) //считает сумму цифр в числе
    {
        int sum = 0;
        while (countnum > 0)
        {
            sum = sum + countnum % 10;
            countnum = countnum / 10;
        }
        return sum;
    }

    public int[] FillArrayFromString(string inputstring) //заполнение целочисленного массива из строки
    {
        string[] temparray = inputstring.Split(" ");
        int[] newarray = new int[temparray.Length];
        for (int i = 0; i < temparray.Length; i++)
        {
            try
            {
                newarray[i] = int.Parse(temparray[i]);
            }
            catch (FormatException)
            {
                newarray[i] = -1;
                throw;
            }
        }
        return newarray;
    }

    public int[] FillRandomArray(int arraylength, int firstnum, int secondnum) //заполнение целочисленного рандомного массива
    {
        int[] newarray = new int[arraylength];
        for (int i = 0; i < arraylength; i++)
            newarray[i] = new Random().Next(firstnum, secondnum);
        return newarray;
    }
    public double[] FillRandomArray(int arraylength, double firstnum, double secondnum) //заполнение массива double рандомно
    {
        double[] newarray = new double[arraylength];
        for (int i = 0; i < arraylength; i++)
        {
            var rnd = new Random();
            newarray[i] = firstnum + rnd.NextDouble() * (secondnum - firstnum);
        }
        return newarray;
    }

    public int GetMaxNumberInArray(int[] newarray) //найти максимум в массиве. 
    {
        int maxnum = newarray[0];
        int size=newarray.Length;
        for (int i = 1; i < size; i++)
            if (newarray[i] > maxnum) maxnum = newarray[i];
        return maxnum;
    }

    public int GetMinNumberInArray(int[] newarray) //найти минимум в массиве. 
    {
        int minnum = newarray[0];
        int size=newarray.Length;
        for (int i = 1; i < size; i++)
            if (newarray[i] < minnum) minnum = newarray[i];
        return minnum;
    }

    public double GetAverageFromArray(int[] newarray) //найти среднее арифм. массива
    {
        int sum = 0;
        int size = newarray.Length;
        for (int i = 0; i < size; i++)
            sum += newarray[i];
        return sum / size;
    }
    public double GetMaxNumberInArray(double[] newarray) //найти максимум в массиве double. 
    {
        double maxnum = newarray[0];
        int size=newarray.Length;
        for (int i = 1; i < size; i++)
            if (newarray[i] > maxnum) maxnum = newarray[i];
        return maxnum;
    }

    public double GetMinNumberInArray(double[] newarray) //найти минимум в массиве double. 
    {
        double minnum = newarray[0];
        int size=newarray.Length;
        for (int i = 1; i < size; i++)
            if (newarray[i] < minnum) minnum = newarray[i];
        return minnum;
    }

    public double GetAverageFromArray(double[] newarray) //найти среднее арифм. массива double
    {
        double sum = 0;
        int size = newarray.Length;
        for (int i = 0; i < size; i++)
            sum += newarray[i];
        return sum / size;
    }

    public int CountEvenNumbers(int[] newarray) //найти кол-во чётных элементов в массиве
    {
        int sum = 0;
        int size = newarray.Length;
        for (int i = 0; i < size; i++)
        {
            if (newarray[i] % 2 == 0) sum ++;
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
    public (int[] evenarray, int[] oddarray) MakeEvenOddArrays(int[] array)
    {
        int size=array.Length;
        List<int> evenarray=new List<int>();
        List<int> oddarray=new List<int>();
        for (int i=0;i<size;i++)
        {
            if (array[i]%2==0) 
                evenarray.Add(array[i]);
            else 
                oddarray.Add(array[i]);
        }
        return (evenarray.ToArray(),oddarray.ToArray());
    }

}

