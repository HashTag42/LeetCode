// LeetCode problem: 14. Longest Common Prefix
// https://leetcode.com/problems/longest-common-prefix/description/

namespace LeetCode.LongestCommonPrefix;

public class Solution
{
    /// <summary>
    /// Find the longest common prefix string among an array of strings.
    /// If there is no common prefix, return an empty string.
    /// </summary>
    public string LongestCommonPrefix(string[] strs)
    {
        if (strs.Length == 0)
            return "";

        // Find the minimum string length
        int minLength = strs.Min(s => s.Length);

        // Check each character position across all strings
        for (int i = 0; i < minLength; i++)
        {
            if (!strs.All(str => str[i] == strs[0][i]))
                return strs[0][..i];
        }

        // All characters matched up to the shortest string
        return strs[0][..minLength];
    }
}