# LeetCode challenge: 14. Longest Common Prefix
# <https://leetcode.com/problems/longest-common-prefix/description/>

class Solution:

    ''' Find the longest common prefix string among an array of strings.
        If there is no common prefix, return an empty string"". '''
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        common_prefix = ""
        i = 0
        while (True):
            if i >= len(strs[0]):
                break
            char = strs[0][i]
            for s in strs:
                if i >= len(s) or char != s[i]:
                    return common_prefix
            common_prefix += char
            i += 1
        return common_prefix
