//Задача про собаку и двух друзей. Алгоритм в тетрадке
int count = 0, distance = 10000, friend = 2, time = 0;
int firstfriendspeed = 1;
int secondfriendspeed = 2;
int dogspeed = 5;
while (distance > 10)
{
    if (friend == 1)
    {
        time = distance / (firstfriendspeed + dogspeed);
        friend = 2;
    }
    else
    {
        time = distance / (secondfriendspeed + dogspeed);
        friend = 1;
    }
    distance = distance - (firstfriendspeed + secondfriendspeed) * time;
    count++;
}
Console.WriteLine("Собака пробежит " + count + " раз");
