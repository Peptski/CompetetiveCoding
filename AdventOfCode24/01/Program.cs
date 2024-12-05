using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main(string[] args)
    {
        string inputFilePath = Path.Combine("Inputs", "input.txt");
        string input = File.ReadAllText(inputFilePath);
        int firstResult = SolveFirstChallenge(input);
        int secondResult = SolveSecondChallenge(input);

        Console.WriteLine($"First Result: {firstResult}");
        Console.WriteLine($"Second Result: {secondResult}");
    }

    static int SolveFirstChallenge(string input)
    {
        input = input.Replace("   ", " ");
        input = input.Replace("\r\n", " ");

        List<string> stringList = input.Split(" ").ToList();
        List<int> intList = stringList.ConvertAll(int.Parse);
        List<int> leftList = intList.Where((x, i) => i % 2 == 0).ToList();
        List<int> rightList = intList.Where((x, i) => i % 2 == 1).ToList();

        leftList.Sort();
        rightList.Sort();

        int sum = 0;

        for (int i = 0; i < leftList.Count; i++)
        {
            sum += Math.Abs(leftList[i] - rightList[i]);
        }

        return sum;
    }

    static int SolveSecondChallenge(string input)
    {
        input = input.Replace("   ", " ");
        input = input.Replace("\r\n", " ");

        List<string> stringList = input.Split(" ").ToList();
        List<int> intList = stringList.ConvertAll(int.Parse);
        List<int> leftList = intList.Where((x, i) => i % 2 == 0).ToList();
        List<int> rightList = intList.Where((x, i) => i % 2 == 1).ToList();

        int sum = 0;

        for (int i = 0; i < leftList.Count; i++)
        {
            for (int j = 0; j < rightList.Count; j++)
            {
                sum += leftList[i] == rightList[j] ? leftList[i] : 0;
            }
        }

        return sum;
    }
}