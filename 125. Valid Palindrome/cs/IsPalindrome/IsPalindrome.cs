/*
LeetCode problem 125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/
*/

namespace LeetCode.IsPalindrome;

public class Solution
{
    public bool IsPalindrome1(string s)
    {
        var cleaned = new string([.. s.Where(char.IsLetterOrDigit).Select(char.ToLower)]);
        return cleaned == new string([.. cleaned.Reverse()]);
    }

    public bool IsPalindrome2(string s)
    {
        int i = 0, j = s.Length - 1;
        while (i < j)
        {
            while (i < j && !char.IsLetterOrDigit(s[i]))
                i++;
            while (i < j && !char.IsLetterOrDigit(s[j]))
                j--;
            if (char.ToLower(s[i]) != char.ToLower(s[j]))
                return false;
            i++;
            j--;
        }
        return true;
    }
}