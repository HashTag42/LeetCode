/*
    LeetCode problem: 9. Palindrome Number
    https://leetcode.com/problems/palindrome-number/description/
*/
namespace LeetCode.IsPalindrome;

public class Solution
{
    public bool IsPalindrome(int x)
    {
        // Complexity: Time = O(n), Space = O(n)
        string strX = x.ToString();
        int lenX = strX.Length;
        for (int i = 0; i < (lenX / 2); i++)
            if (strX[i] != strX[lenX - 1 - i])
                return false;
        return true;
    }
}