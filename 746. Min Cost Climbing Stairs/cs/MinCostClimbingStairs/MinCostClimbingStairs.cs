namespace LeetCode.MinCostClimbingStairs;

public class MinCostClimbingStairs
{
    // Return the minimum cost to reach the top of the floor.
    // Complexity:
    //      Time: O(n)
    //      Space: O(1)
    public static int Calculate(int[] cost)
    {
        int prev2 = cost[0];    // min cost to reach step 0
        int prev1 = cost[1];    // min cost to reach step 1

        for (int i = 2; i < cost.Length; i++)
        {
            int current = cost[i] + Math.Min(prev1, prev2);
            prev2 = prev1;
            prev1 = current;
        }

        return Math.Min(prev1, prev2);
    }
}