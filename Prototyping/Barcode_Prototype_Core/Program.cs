using System;

namespace Barcode_Prototype_Core
{
    class Program
    {
        static void Main(string[] args)
        {
            bool scan = true;
            Console.WriteLine("Start Scanning");
            while (scan == true)
            {
                Console.ReadLine();
                Console.WriteLine("\nScan again? (1=yes)");
                if (Console.ReadLine() != "1")
                {
                    scan = false;
                }

            }
        }
    }
}
