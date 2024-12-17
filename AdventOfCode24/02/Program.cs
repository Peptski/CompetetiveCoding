class Program
{
  static void Main(string[] args)
  {
    string inputFilePath = Path.Combine("input", "data.txt");
    string input = File.ReadAllText(inputFilePath);

    var reports = ParseInput(input);

    int firstResult = SolveFirstChallenge(reports);
    int secondResult = SolveSecondChallenge(reports);

    Console.WriteLine($"First Result: {firstResult}");
    Console.WriteLine($"Second Result: {secondResult}");
  }

  static List<List<int>> ParseInput(string input)
  {
    var reports = input.Split(['\r', '\n'], StringSplitOptions.RemoveEmptyEntries).ToList();

    var nestedArrayOfReports = reports.Select(report => report.Split(' ').Select(int.Parse).ToList()).ToList();

    return nestedArrayOfReports;
  }

  static Boolean SolveReport(List<int> report)
  {
    if (report.SequenceEqual(report.Order()) || report.SequenceEqual(report.OrderDescending()))
    {
      int reportCount = report.Count;

      for (int i = 0; i < reportCount - 1; i++)
      {
        var distance = Math.Abs(report[i] - report[i + 1]);

        if (distance > 3 || distance <= 0) { return false; }
      }

      return true;
    }

    return false;
  }

  static int SolveFirstChallenge(List<List<int>> reports)
  {
    var safeReports = 0;

    foreach (var report in reports)
    {
      var safe = SolveReport(report);

      safeReports += safe ? 1 : 0;
    }

    return safeReports;
  }

  static int SolveSecondChallenge(List<List<int>> reports)
  {
    var safeReports = 0;

    foreach (var report in reports)
    {
      var safe = SolveReport(report);

      if (!safe)
      {
        for (int i = 0; i < report.Count; i++)
        {
          if (SolveReport(report.Where((number, index) => index != i).ToList()))
          {
            safeReports += 1;
            break;
          }
        }
      }

      safeReports += safe ? 1 : 0;
    }

    return safeReports;
  }
}