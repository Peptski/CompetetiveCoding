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

        var (leftList, rightList) = ParseInput(input);

        int firstResult = SolveFirstChallenge(leftList, rightList);
        int secondResult = SolveSecondChallenge(leftList, rightList);

        Console.WriteLine($"First Result: {firstResult}");
        Console.WriteLine($"Second Result: {secondResult}");
    }

    static (List<int> leftList, List<int> rightList) ParseInput(string input)
    {
        var numbers = input.Split(new[] { ' ', '\n', '\r' }, StringSplitOptions.RemoveEmptyEntries)
                           .Select(int.Parse)
                           .ToList();

        var leftList = numbers.Where((_, i) => i % 2 == 0).ToList();
        var rightList = numbers.Where((_, i) => i % 2 == 1).ToList();

        return (leftList, rightList);
    }

    static int SolveFirstChallenge(List<int> leftList, List<int> rightList)
    {
        leftList.Sort();
        rightList.Sort();

        int sum = leftList.Zip(rightList, (left, right) => Math.Abs(left - right)).Sum();
        return sum;
    }

    static int SolveSecondChallenge(List<int> leftList, List<int> rightList)
    {
        var rightCounts = rightList.GroupBy(x => x).ToDictionary(g => g.Key, g => g.Count());

        int sum = leftList.Sum(left => left * (rightCounts.ContainsKey(left) ? rightCounts[left] : 0));

        return sum;
    }
}