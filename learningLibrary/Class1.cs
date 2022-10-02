namespace learningLibrary;
public class myLearningClass
{
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
}

