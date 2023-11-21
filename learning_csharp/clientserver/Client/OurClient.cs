using System.Text;
using System.Net.Sockets;

namespace Client
{
    class OurClient
    {
        private TcpClient client;
        StreamWriter sWriter;
        public OurClient()
        {
            client=new TcpClient("127.0.0.1",5555); //сделали нового клиента
            sWriter=new StreamWriter(client.GetStream(),Encoding.UTF8); //получили его поток

            HandleCommunication();
        }

        void HandleCommunication() //это чтоб соединение висело постоянно
        {
            while(true)
            {
                Console.Write("> ");
                string? message = Console.ReadLine();
                sWriter.WriteLine(message); //просто строчку пишем и отправляем клиенту. пинг
                sWriter.Flush(); //отправка буфера
            }
        }
    }
}