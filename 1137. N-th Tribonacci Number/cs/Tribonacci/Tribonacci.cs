namespace LeetCode.Tribonacci;

public class Tribonacci
{
    public static int Calculate(int num)
    {
        List<int> results = [0, 1, 1];
        for (int i = 3; i <= num; i++)
        {
            results.Add(results[^1] + results[^2] + results[^3]);
        }
        return results[num];
    }
}