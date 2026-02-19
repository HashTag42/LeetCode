/*
    LeetCode challenge: 3. Longest Substring Without Repeating Characters
    https://leetcode.com/problems/longest-substring-without-repeating-characters/description
*/
namespace LeetCode.LengthOfLongestSubstring;

public class Solution
{
    // Sliding window approach
    // Time Complexity: O(N)
    // Space Complexity: O(min(N, M)) where M is the charset size
    public static int LengthOfLongestSubstring(string s)
    {
        Dictionary<char, int> charIndex = [];
        int left = 0;
        int maxLen = 0;

        for (int right = 0; right < s.Length; right++)
        {
            char c = s[right];
            if (charIndex.TryGetValue(c, out int idx) && idx >= left)
                left = idx + 1;
            charIndex[c] = right;
            maxLen = Math.Max(maxLen, right - left + 1);
        }

        return maxLen;
    }
}

