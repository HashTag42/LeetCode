// LeetCode problem 35. Search Insert Position
// https://leetcode.com/problems/search-insert-position/

namespace LeetCode.SearchInsert;

public class Solution
{
    public int SearchInsert(int[] nums, int target)
    {
        int low = 0;
        int high = nums.Length - 1;

        while (low <= high)
        {
            int mid = (low + high) / 2;
            if (nums[mid] == target)
                return mid; // Found
            else if (nums[mid] < target)
                low = mid + 1;  // Search right half
            else
                high = mid - 1; // Search left half
        }
        return low; // Not found
    }
}