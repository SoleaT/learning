Console.WriteLine("Программа приветствия конкретного пользователя");
Console.Write("Введите имя пользователя: ");
string username = Console.ReadLine();
if (username.ToLower() == "вася")
{
    Console.WriteLine("Привет, Васян! Давно не виделись. Как оно?");
}
else
{
    Console.WriteLine("Здравствуйте, пользователь " + username);
}