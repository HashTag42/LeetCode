# LeetCode challenge: 14. Longest Common Prefix
# <https://leetcode.com/problems/longest-common-prefix/description/>

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ''' Find the longest common prefix string among an array of strings.
            If there is no common prefix, return an empty string"". '''
        if not strs:
            return ""
        for i, chars in enumerate(zip(*strs)):
            if len(set(chars)) > 1:
                return strs[0][:i]
        return min(strs)  # All chars matched up to shortest string
