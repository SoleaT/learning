// Написать программу, которая будет выдавать название дня недели по заданному номеру
Console.Write("Введите номер дня недели: ");
int weekdaynum = int.Parse(Console.ReadLine());
string[] dayofweek = { "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье" };
if (weekdaynum < 1 || weekdaynum > 7)
{
    Console.WriteLine("Неправильно задан номер дня недели. Остаётесь без ответа.");
}
else
{
    Console.WriteLine("Ваш день недели - " + dayofweek[weekdaynum-1]);
}
