using System;

class Program
{
    static string AverageOne()
    {
        double a = double.Parse(Console.ReadLine());
        double b = double.Parse(Console.ReadLine());

        double weightOfA = 3.5;
        double weightOfB = 7.5;

        double media = (a * weightOfA + b * weightOfB) / (weightOfA + weightOfB);

        return $"MEDIA = {media:F5}";
    }

    static void Main()
    {
        Console.WriteLine(AverageOne());
    }
}