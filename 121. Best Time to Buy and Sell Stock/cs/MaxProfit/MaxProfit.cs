// LeetCode problem: 121. Best Time to Buy and Sell Stock
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

namespace LeetCode.MaxProfit;

public class Solution
{
    public int MaxProfit(int[] prices)
    {
        /*
        Constraints:
            1 <= prices.length <= 105
            0 <= prices[i] <= 104
        */
        int minPrice = prices[0];
        int maxProfit = 0;
        foreach (var price in prices)
        {
            if (price < minPrice)
                minPrice = price;
            else
                maxProfit = Math.Max(maxProfit, price - minPrice);
        }
        return maxProfit;
    }
}