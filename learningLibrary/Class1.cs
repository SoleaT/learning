namespace learningLibrary;

//функции нахождения максимума и минимума, заполнения массива строкой - неактуальны
public class myLearningClass
{
    ///<summary>
    ///Ввод числа
    ///</summary>
    ///<returns>Проверенное целое число</returns>
    public int InputNumbers()
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


    ///<summary>
    ///Сумма цифр в числе
    ///</summary>
    ///<param name="countNum">Число</param>
    ///<returns>Сумма цифр</returns>
    public int CountDigits(int countNum)
    {
        int sum = 0;
        while (countNum > 0)
        {
            sum = sum + countNum % 10;
            countNum = countNum / 10;
        }
        //вариант математический - логарифм по основанию 10 показывает в какую степень 
        //возвести 10, чтоб получить число. округляем до большего
        //double sum=Math.Ceiling(Math.Log10(countNum))
        return sum;
    }

    #region FillArrays

    // замены этой функции, но без проверки на вшивость:
    // int[] inputArray = Array.ConvertAll(Console.ReadLine().Split(" "), int.Parse);
    // int[] inputArray = Console.ReadLine()!.Split(separators).Select(int.Parse).ToArray();
    ///<summary>
    ///Заполнение одномерного целочисленного массива из строки
    ///</summary>
    public int[] FillArrayFromString(string inputstring)
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

    ///<summary>
    ///Заполнение одномерного целочисленного массива случайно
    ///</summary>
    ///<param name="size">Размер массива</param>
    ///<param name="firstNum">начиная с числа</param>
    ///<param name="secondNum">заканчивая числом</param>
    ///<returns>Массив</returns>
    public int[] FillRandomArray(int size, int firstNum, int secondNum)
    {
        int[] newArray = new int[size];
        for (int i = 0; i < size; i++)
            newArray[i] = new Random().Next(firstNum, secondNum);
        return newArray;
    }
    ///<summary>
    ///Заполнение одномерного вещественного массива случайно
    ///</summary>
    ///<param name="size">Размер массива</param>
    ///<param name="firstNum">начиная с числа</param>
    ///<param name="secondNum">заканчивая числом</param>
    ///<returns>Массив</returns>
    public double[] FillRandomArray(int size, double firstNum, double secondNum)
    {
        double[] newArray = new double[size];
        for (int i = 0; i < size; i++)
        {
            var rnd = new Random();
            newArray[i] = firstNum + rnd.NextDouble() * (secondNum - firstNum);
        }
        return newArray;
    }

    ///<summary>
    ///Заполнение двумерного массива случайно
    ///</summary>
    ///<param name="int[,]">Целочисленный массив</param>
    ///<param name="firstNum">начиная с числа</param>
    ///<param name="secondNum">заканчивая числом</param>
    ///<returns></returns>
    public void FillRandomArray(int[,] tempArray, int firstNum, int secondNum)
    {
        int rows = tempArray.GetLength(0);
        int cols = tempArray.GetLength(1);
        var r = new Random();
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                tempArray[i, j] = r.Next(firstNum, secondNum);
            }
        }
        // return tempArray;
    }

    ///<summary>
    ///Заполнение двумерного массива случайно
    ///</summary>
    ///<param name="double[,]">Вещественный массив</param>
    ///<param name="firstNum">начиная с числа</param>
    ///<param name="secondNum">заканчивая числом</param>
    ///<returns></returns>
    public void FillRandomArray(double[,] tempArray,
                                double firstNum,
                                double secondNum)
    {
        int rows = tempArray.GetLength(0);
        int cols = tempArray.GetLength(1);
        var r = new Random();
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                tempArray[i, j] = Math.Round(firstNum + r.NextDouble() * (secondNum - firstNum), 2);
            }
        }
    }

    #endregion

    #region Print

    ///<summary>
    ///Печать двумерного массива
    ///</summary>
    ///<param name="int[,]">Целочисленный массив</param>
    ///<returns></returns>
    public void PrintMatrix(int[,] tempArray)
    {
        int rows = tempArray.GetLength(0);
        int cols = tempArray.GetLength(1);
        for (int i = 0; i < rows; i++)
        {
            System.Console.Write("[");
            for (int j = 0; j < cols; j++)
            {
                System.Console.Write("{0,3}",tempArray[i, j]);
            }
            System.Console.WriteLine("]");
        }
    }

    ///<summary>
    ///Печать двумерного массива
    ///</summary>
    ///<param name="double[,]">Вещественный массив</param>
    ///<returns></returns>
    public void PrintMatrix(double[,] tempArray) //печать двумерного массива
    {
        int rows = tempArray.GetLength(0);
        int cols = tempArray.GetLength(1);
        for (int i = 0; i < rows; i++)
        {
            System.Console.Write("[");
            for (int j = 0; j < cols; j++)
            {
                System.Console.Write($"{tempArray[i, j]} ");
            }
            System.Console.WriteLine("]");
        }
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

    ///<summary>
    ///Возвращает количество чётных элементов в массиве
    ///</summary>
    ///<param name="newArray">массив int[]</param>
    ///<returns>Количество</returns>
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

    ///<summary>
    ///найти сумму элементов массива на чётных позициях
    ///</summary>
    ///<param name="array">массив int[]</param>
    ///<returns>Сумма</returns>    
    public int CountSumOnEvenPositions(int[] array)
    {
        int sum = 0;
        int size = array.Length;
        for (int i = 0; i < size; i++)
            if (i % 2 != 0) sum += array[i];
        return sum;
    }

    ///<summary>
    ///делим массив на 2 массива: четных и нечетных чисел
    ///</summary>
    ///<param name="array">массив int[]</param>
    ///<returns>(evenArray,oddArray) - кортеж массивов</returns> 
    public (int[] evenArray, int[] oddArray) MakeEvenoddArrays(int[] array) //
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

}

