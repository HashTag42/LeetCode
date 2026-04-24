/*
LeetCode problem 242. Valid Anagram
https://leetcode.com/problems/valid-anagram/description/
*/

namespace LeetCode.IsAnagram;

public class Solution
{
    public bool IsAnagram(string s, string t)
    {
        int[] count = new int[26];
        foreach (var c in s) count[c - 'a']++;
        foreach (var c in t) count[c - 'a']--;
        return count.All(x => x == 0);
    }
}